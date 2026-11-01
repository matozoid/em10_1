// Decompile the functions containing the given runtime addresses (script args, hex).
import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.*;
import ghidra.program.model.listing.*;

public class DecompAt extends GhidraScript {
    @Override
    protected void run() throws Exception {
        DecompInterface di = new DecompInterface();
        di.openProgram(currentProgram);
        for (String a : getScriptArgs()) {
            Function f = getFunctionContaining(toAddr(Long.decode(a)));
            if (f == null) { println("// no function at " + a); continue; }
            DecompileResults r = di.decompileFunction(f, 120, monitor);
            println("// ===== " + f.getName() + " @ " + f.getEntryPoint());
            println(r.decompileCompleted() ? r.getDecompiledFunction().getC() : "// decompile failed: " + r.getErrorMessage());
        }
    }
}
