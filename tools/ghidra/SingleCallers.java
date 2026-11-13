// For every function with exactly one reference to its entry, write  callee <TAB> caller function <TAB>
// reference type <TAB> call-site address  to the file arg0. Functions whose single reference is not from
// inside a function (a data pointer, a vtable slot) are written with caller "-".
// usage: -postScript SingleCallers.java /path/out.tsv   (read-only)
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.symbol.Reference;
import java.io.PrintWriter;

public class SingleCallers extends GhidraScript {
    @Override
    protected void run() throws Exception {
        int n = 0;
        try (PrintWriter w = new PrintWriter(getScriptArgs()[0])) {
            FunctionIterator it = currentProgram.getFunctionManager().getFunctions(true);
            while (it.hasNext()) {
                Function f = it.next();
                Reference[] refs = getReferencesTo(f.getEntryPoint());
                if (refs.length != 1) continue;
                Function c = currentProgram.getFunctionManager().getFunctionContaining(refs[0].getFromAddress());
                w.println(String.format("%s\t%s\t%s\t%s", f.getEntryPoint(), c == null ? "-" : c.getEntryPoint().toString(),
                    refs[0].getReferenceType(), refs[0].getFromAddress()));
                n++;
            }
        }
        println("single-reference functions: " + n);
    }
}
