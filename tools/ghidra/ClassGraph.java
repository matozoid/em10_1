// Inheritance + constructor naming from vtable candidates (arg0 = vtables.tsv from VTables.java, arg1 = output tsv, arg2 = "rename" optional).
// A candidate counts as a class vtable if code references its start (ctor/dtor stores it) or it has a class vote.
// Parent = other class vtable sharing the most identical slots at the same index (>=2 shared and >=50% of the shorter table),
// ignoring functions that appear in >40 tables (stubs). Unnamed class -> "cls_<addr>"; methods/ctors renamed <class>__vfnN / __ctordtor.
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.*;
import ghidra.program.model.listing.*;
import ghidra.program.model.symbol.*;
import java.io.*;
import java.util.*;

public class ClassGraph extends GhidraScript {
    static class V { long addr; int n; String cls; long[] slots; List<Function> ctors = new ArrayList<>(); V parent; int shared; String name; }
    @Override
    protected void run() throws Exception {
        boolean rename = getScriptArgs().length > 2 && getScriptArgs()[2].equals("rename");
        FunctionManager fm = currentProgram.getFunctionManager();
        List<V> all = new ArrayList<>();
        try (BufferedReader r = new BufferedReader(new FileReader(getScriptArgs()[0]))) {
            r.readLine(); String l;
            while ((l = r.readLine()) != null) {
                String[] t = l.split("\t", -1);
                V v = new V(); v.addr = Long.parseLong(t[0], 16); v.n = Integer.parseInt(t[1]); v.cls = t[2];
                String[] m = t[4].split(",");
                v.slots = new long[v.n];
                for (int i = 0; i < v.n; i++) v.slots[i] = Long.parseLong(m[i], 16);
                for (Reference rf : getReferencesTo(toAddr(v.addr))) {
                    Function c = getFunctionContaining(rf.getFromAddress());
                    if (c != null && !v.ctors.contains(c)) v.ctors.add(c);
                }
                all.add(v);
            }
        }
        // class vtables
        List<V> cl = new ArrayList<>();
        for (V v : all) if (!v.ctors.isEmpty() || !v.cls.isEmpty()) cl.add(v);
        println("candidates " + all.size() + " class vtables " + cl.size());
        // slot index
        Map<String, List<V>> idx = new HashMap<>();
        Map<Long, Integer> freq = new HashMap<>();
        for (V v : cl) for (long s : v.slots) freq.merge(s, 1, Integer::sum);
        for (V v : cl) for (int i = 0; i < v.n; i++) if (freq.get(v.slots[i]) <= 40) idx.computeIfAbsent(i + ":" + v.slots[i], k -> new ArrayList<>()).add(v);
        for (V v : cl) {
            Map<V, Integer> sc = new HashMap<>();
            for (int i = 0; i < v.n; i++) {
                List<V> b = idx.get(i + ":" + v.slots[i]);
                if (b == null) continue;
                for (V o : b) if (o != v) sc.merge(o, 1, Integer::sum);
            }
            V best = null; int bs = 0;
            for (Map.Entry<V, Integer> e : sc.entrySet()) {
                V o = e.getKey(); int s = e.getValue();
                if (o.n > v.n) continue;                       // parent no longer than child
                if (o.n == v.n && o.addr > v.addr) continue;  // tie-break to avoid 2-cycles
                if (s < 2 || s * 2 < o.n) continue;
                if (s > bs || (s == bs && best != null && o.n > best.n)) { best = o; bs = s; }
            }
            v.parent = best; v.shared = bs;
        }
        // names
        // Voted names are polluted by inherited base methods: only the first (shortest, lowest address) table of a name keeps it;
        // others become <name>_sub<addr>. Unvoted -> cls_<addr>.
        List<V> byOrder = new ArrayList<>(cl);
        byOrder.sort(Comparator.comparingInt((V x) -> x.n).thenComparingLong(x -> x.addr));
        Set<String> used = new HashSet<>();
        for (V v : byOrder) {
            if (v.cls.isEmpty()) v.name = "cls_" + Long.toHexString(v.addr);
            else if (used.add(v.cls)) v.name = v.cls;
            else v.name = v.cls + "_sub" + Long.toHexString(v.addr);
        }
        int roots = 0, edges = 0, renamed = 0;
        List<V> order = new ArrayList<>(cl);
        order.sort(Comparator.comparingInt((V x) -> x.n).thenComparingLong(x -> x.addr));
        try (PrintWriter w = new PrintWriter(new FileWriter(getScriptArgs()[1]))) {
            w.println("vtable\tslots\tclass\tvoted\tparent\tshared\tctors");
            for (V v : order) {
                if (v.parent == null) roots++; else edges++;
                StringBuilder cs = new StringBuilder();
                for (Function c : v.ctors) cs.append(c.getName()).append(' ');
                w.println(Long.toHexString(v.addr) + "\t" + v.n + "\t" + v.name + "\t" + (v.cls.isEmpty() ? "" : "y") + "\t" +
                    (v.parent == null ? "" : v.parent.name + "@" + Long.toHexString(v.parent.addr)) + "\t" + v.shared + "\t" + cs);
                if (rename) {
                    for (int i = 0; i < v.n; i++) {
                        Function f = fm.getFunctionAt(toAddr(v.slots[i]));
                        if (f != null && f.getName().startsWith("FUN_") && freq.get(v.slots[i]) <= 40) {
                            try { f.setName(v.name + "__vfn" + i + "_" + f.getEntryPoint(), SourceType.ANALYSIS); renamed++; } catch (Exception e) {}
                        }
                    }
                    for (Function c : v.ctors) if (c.getName().startsWith("FUN_")) {
                        try { c.setName(v.name + "__ctordtor_" + c.getEntryPoint(), SourceType.ANALYSIS); renamed++; } catch (Exception e) {}
                    }
                }
            }
        }
        println("roots " + roots + " with parent " + edges + " renamed " + renamed);
    }
}
