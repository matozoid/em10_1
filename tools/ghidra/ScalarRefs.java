// List instructions whose scalar operand is in [arg0, arg1) with containing function. usage: -postScript ScalarRefs.java 0xbf000000 0xc0000000
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.*;
import ghidra.program.model.scalar.Scalar;

public class ScalarRefs extends GhidraScript {
    @Override
    protected void run() throws Exception {
        long lo = Long.decode(getScriptArgs()[0]), hi = Long.decode(getScriptArgs()[1]);
        for (Instruction in : currentProgram.getListing().getInstructions(true)) {
            for (int i = 0; i < in.getNumOperands(); i++)
                for (Object o : in.getOpObjects(i))
                    if (o instanceof Scalar) {
                        long v = ((Scalar) o).getUnsignedValue();
                        if (v >= lo && v < hi) {
                            Function f = currentProgram.getFunctionManager().getFunctionContaining(in.getAddress());
                            println(String.format("%s %08x %s", in.getAddress(), v, f == null ? "-" : f.getName()));
                        }
                    }
        }
    }
}
