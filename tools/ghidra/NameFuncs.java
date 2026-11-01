// Auto-name default-named (FUN_*) or previously auto-named (*_<8hex>) functions from strings they reference.
// Heuristic: first referenced string containing an identifier token (>=6 chars, has '_' or inner capital, not a format spec).
// Name = <ident>_<entry hex>. Writes TSV (arg0): entry, new name, source string. Idempotent: only touches FUN_* names.
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.*;
import ghidra.program.model.address.*;
import ghidra.program.model.symbol.*;
import java.io.*;
import java.util.*;
import java.util.regex.*;

public class NameFuncs extends GhidraScript {
    static final Pattern ID = Pattern.compile("(?<![A-Za-z0-9_%])([A-Za-z_][A-Za-z0-9_]{5,40})(?![A-Za-z0-9_])");
    static final Pattern CPP = Pattern.compile("([A-Za-z_][A-Za-z0-9_]{2,40})::(~?[A-Za-z_][A-Za-z0-9_]{1,40})");
    String strAt(Address a) throws Exception {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 120; i++) {
            int c = getByte(a.add(i)) & 0xff;
            if (c == 0) break;
            if (c < 0x20 || c > 0x7e) return null;
            sb.append((char) c);
        }
        return sb.length() >= 6 ? sb.toString() : null;
    }
    String ident(String s) {
        Matcher c = CPP.matcher(s);
        if (c.find()) return c.group(1) + "__" + c.group(2).replace("~", "dtor_");
        Matcher m = ID.matcher(s);
        String fallback = null;
        while (m.find()) {
            String t = m.group(1);
            boolean good = t.indexOf('_') > 0 || t.matches(".*[a-z][A-Z].*");
            if (good && !t.matches("(?i)0x.*|err_?.*")) return t;
            if (fallback == null && t.matches("[A-Za-z]+") && t.length() >= 7) fallback = t;
        }
        return fallback;
    }
    @Override
    protected void run() throws Exception {
        ReferenceManager rm = currentProgram.getReferenceManager();
        int named = 0;
        try (PrintWriter w = new PrintWriter(new FileWriter(getScriptArgs()[0]))) {
            w.println("entry\tname\tsource");
            for (Function f : currentProgram.getFunctionManager().getFunctions(true)) {
                if (!(f.getName().startsWith("FUN_") || f.getName().matches(".*_[0-9a-f]{8}$"))) continue;
                String src = null, id = null;
                AddressIterator it = rm.getReferenceSourceIterator(f.getBody(), true);
                outer:
                while (it.hasNext()) {
                    for (Reference r : rm.getReferencesFrom(it.next())) {
                        if (r.getReferenceType().isCall()) continue;
                        Address t = r.getToAddress();
                        if (!t.isMemoryAddress() || !currentProgram.getMemory().contains(t)) continue;
                        String s = null;
                        try { s = strAt(t); } catch (Exception e) {}
                        if (s == null) continue;
                        String i = ident(s);
                        if (i != null) { src = s; id = i; break outer; }
                    }
                }
                if (id == null) continue;
                String nm = id + "_" + f.getEntryPoint().toString();
                if (f.getName().equals(nm)) continue;
                try { f.setName(nm, SourceType.ANALYSIS); named++; } catch (Exception e) { continue; }
                w.println(f.getEntryPoint() + "\t" + nm + "\t" + src.replace("\t", " "));
            }
        }
        println("named " + named);
    }
}
