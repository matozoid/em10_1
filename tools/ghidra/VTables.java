// Find vtable-like arrays: >=3 consecutive aligned u32 that are function entry points, outside disassembled code.
// Output TSV (arg0): addr, count, class vote (majority "Class" of members named Class__*), members.
// With arg1 = "rename": names unnamed members Class__vfn<i>_<addr> and referencing FUN_* (ctor/dtor) Class__ctordtor_<addr>
// when >=60% of named members agree on the class (tentative: shared base methods can mislead).
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.*;
import ghidra.program.model.listing.*;
import ghidra.program.model.mem.*;
import ghidra.program.model.symbol.SourceType;
import java.io.*;
import java.util.*;

public class VTables extends GhidraScript {
    @Override
    protected void run() throws Exception {
        boolean rename = getScriptArgs().length > 1 && getScriptArgs()[1].equals("rename");
        FunctionManager fm = currentProgram.getFunctionManager();
        Listing li = currentProgram.getListing();
        Memory mem = currentProgram.getMemory();
        int nv = 0, renamed = 0;
        try (PrintWriter w = new PrintWriter(new FileWriter(getScriptArgs()[0]))) {
            w.println("addr\tcount\tclass\tvotes\tmembers");
            for (MemoryBlock b : mem.getBlocks()) {
                if (!b.isInitialized()) continue;
                long start = b.getStart().getOffset(), end = b.getEnd().getOffset();
                start = (start + 3) & ~3L;
                long a = start;
                while (a + 12 <= end) {
                    List<Function> run = new ArrayList<>();
                    long p = a;
                    while (p + 4 <= end) {
                        Address pa = toAddr(p);
                        if (li.getInstructionContaining(pa) != null) break;
                        long v = mem.getInt(pa) & 0xffffffffL;
                        Function f = fm.getFunctionAt(toAddr(v));
                        if (f == null) break;
                        run.add(f);
                        p += 4;
                    }
                    if (run.size() >= 3) {
                        nv++;
                        Map<String, Integer> votes = new HashMap<>();
                        int named = 0;
                        for (Function f : run) {
                            int i = f.getName().indexOf("__");
                            if (i > 0) { votes.merge(f.getName().substring(0, i), 1, Integer::sum); named++; }
                        }
                        String cls = "", vs = "";
                        for (Map.Entry<String, Integer> e : votes.entrySet())
                            if (e.getValue() > (cls.isEmpty() ? 0 : votes.get(cls))) cls = e.getKey();
                        if (!cls.isEmpty()) vs = votes.get(cls) + "/" + run.size();
                        StringBuilder sb = new StringBuilder();
                        for (Function f : run) sb.append(f.getEntryPoint()).append(',');
                        w.println(toAddr(a) + "\t" + run.size() + "\t" + cls + "\t" + vs + "\t" + sb);
                        if (rename && !cls.isEmpty() && named >= 1 && votes.get(cls) * 10 >= named * 6) {
                            for (int i = 0; i < run.size(); i++) {
                                Function f = run.get(i);
                                if (f.getName().startsWith("FUN_") || (f.getName().matches(".*_[0-9a-f]{8}$") && !f.getName().contains("__"))) {
                                    try { f.setName(cls + "__vfn" + i + "_" + f.getEntryPoint(), SourceType.ANALYSIS); renamed++; } catch (Exception e) {}
                                }
                            }
                            for (ghidra.program.model.symbol.Reference rf : getReferencesTo(toAddr(a))) {
                                Function c = getFunctionContaining(rf.getFromAddress());
                                if (c != null && c.getName().startsWith("FUN_")) {
                                    try { c.setName(cls + "__ctordtor_" + c.getEntryPoint(), SourceType.ANALYSIS); renamed++; } catch (Exception e) {}
                                }
                            }
                        }
                        a = p;
                    } else a += 4;
                }
            }
        }
        println("vtables " + nv + " renamed " + renamed);
    }
}
