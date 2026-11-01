// For vtable candidates in arg0 TSV (from VTables.java), print referencing functions (ctors) for rows with count>=arg1 and a class vote.
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.*;
import ghidra.program.model.symbol.*;
import java.io.*;
import java.util.*;

public class VtRefs extends GhidraScript {
    @Override
    protected void run() throws Exception {
        int n = 0, withref = 0;
        try (BufferedReader r = new BufferedReader(new FileReader(getScriptArgs()[0]))) {
            r.readLine();
            String l;
            while ((l = r.readLine()) != null) {
                String[] t = l.split("\t", -1);
                n++;
                Reference[] refs = getReferencesTo(toAddr(Long.parseLong(t[0], 16)));
                if (refs.length > 0) withref++;
                if (!t[2].isEmpty() && n % 1 == 0) {
                    StringBuilder sb = new StringBuilder();
                    for (Reference f : refs) {
                        Function fn = getFunctionContaining(f.getFromAddress());
                        sb.append(fn == null ? "?" : fn.getName()).append(' ');
                    }
                    println(t[0] + " " + t[1] + " " + t[2] + " refs=" + refs.length + " : " + sb);
                }
            }
        }
        println("rows " + n + " with code refs " + withref);
    }
}
