// Print function count and first N functions with sizes and caller counts (arg0 = N).
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.*;

public class ListFuncs extends GhidraScript {
    @Override
    protected void run() throws Exception {
        int n = getScriptArgs().length > 0 ? Integer.parseInt(getScriptArgs()[0]) : 30;
        FunctionManager fm = currentProgram.getFunctionManager();
        println("functions: " + fm.getFunctionCount());
        int i = 0;
        for (Function f : fm.getFunctions(true)) {
            if (i++ >= n) break;
            println(f.getEntryPoint() + " " + f.getName() + " size=" + f.getBody().getNumAddresses() + " callers=" + f.getSymbol().getReferenceCount());
        }
    }
}
