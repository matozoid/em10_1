// List instructions that reference address arg0 (data xrefs), with containing function and R/W.
// usage: -postScript DataRefs.java 0x8050
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.*;
import ghidra.program.model.symbol.*;

public class DataRefs extends GhidraScript {
    @Override
    protected void run() throws Exception {
        Address target = toAddr(Long.decode(getScriptArgs()[0]));
        ReferenceManager rm = currentProgram.getReferenceManager();
        for (Reference r : rm.getReferencesTo(target)) {
            Address from = r.getFromAddress();
            Function f = currentProgram.getFunctionManager().getFunctionContaining(from);
            Instruction in = currentProgram.getListing().getInstructionAt(from);
            println(String.format("%s %s %s %s", from,
                r.getReferenceType().toString(),
                f == null ? "-" : f.getName(),
                in == null ? "" : in.toString()));
        }
    }
}
