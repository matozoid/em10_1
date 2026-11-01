// List callers (with call-site address) of the function at runtime address arg0. usage: -postScript Callers.java 0x7db66a1c
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.symbol.*;

public class Callers extends GhidraScript {
    @Override
    protected void run() throws Exception {
        Address a = toAddr(Long.decode(getScriptArgs()[0]));
        for (Reference r : getReferencesTo(a)) {
            Function f = currentProgram.getFunctionManager().getFunctionContaining(r.getFromAddress());
            println(String.format("%s %s %s", r.getFromAddress(), r.getReferenceType(), f == null ? "-" : f.getName()));
        }
    }
}
