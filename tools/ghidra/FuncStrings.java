// Export TSV: function entry, size, callers, callees, referenced printable strings (len>=5). arg0 = output file.
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.*;
import ghidra.program.model.address.*;
import ghidra.program.model.symbol.*;
import java.io.*;
import java.util.*;

public class FuncStrings extends GhidraScript {
    String strAt(Address a) throws Exception {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 120; i++) {
            int c = getByte(a.add(i)) & 0xff;
            if (c == 0) break;
            if (c < 0x20 || c > 0x7e) return null;
            sb.append((char) c);
        }
        return sb.length() >= 5 ? sb.toString() : null;
    }
    @Override
    protected void run() throws Exception {
        try (PrintWriter w = new PrintWriter(new FileWriter(getScriptArgs()[0]))) {
            w.println("entry\tsize\tcallers\tcallees\tstrings");
            ReferenceManager rm = currentProgram.getReferenceManager();
            for (Function f : currentProgram.getFunctionManager().getFunctions(true)) {
                LinkedHashSet<String> ss = new LinkedHashSet<>();
                int callees = 0;
                AddressIterator it = rm.getReferenceSourceIterator(f.getBody(), true);
                while (it.hasNext()) {
                    for (Reference r : rm.getReferencesFrom(it.next())) {
                        if (r.getReferenceType().isCall()) { callees++; continue; }
                        Address t = r.getToAddress();
                        if (!t.isMemoryAddress() || !currentProgram.getMemory().contains(t)) continue;
                        String s = null;
                        try { s = strAt(t); } catch (Exception e) {}
                        if (s != null && ss.size() < 8) ss.add(s.replace("\t", " "));
                    }
                }
                w.println(f.getEntryPoint() + "\t" + f.getBody().getNumAddresses() + "\t" + f.getSymbol().getReferenceCount() + "\t" + callees + "\t" + String.join(" | ", ss));
            }
        }
        println("done");
    }
}
