// Find small functions that mask with 0xf and shift by 4 (candidate nibble/RLE decoders).
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.*;
import ghidra.program.model.scalar.Scalar;

public class NibbleFuncs extends GhidraScript {
    @Override
    protected void run() throws Exception {
        int maxLen = Integer.parseInt(getScriptArgs()[0]);
        for (Function f : currentProgram.getFunctionManager().getFunctions(true)) {
            long len = f.getBody().getNumAddresses();
            if (len > maxLen) continue;
            int and15 = 0, sh4 = 0, back = 0;
            for (Instruction in : currentProgram.getListing().getInstructions(f.getBody(), true)) {
                String m = in.getMnemonicString();
                boolean s15 = false, s4 = false;
                for (int i = 0; i < in.getNumOperands(); i++)
                    for (Object o : in.getOpObjects(i))
                        if (o instanceof Scalar) { long v = ((Scalar) o).getUnsignedValue(); if (v == 0xf) s15 = true; if (v == 4) s4 = true; }
                if (m.startsWith("and") && s15) and15++;
                if ((m.startsWith("lsr") || m.startsWith("asr") || m.startsWith("asl")) && s4) sh4++;
                if (m.startsWith("b") && in.getFlowType().isConditional() && in.getFlows().length > 0
                    && in.getFlows()[0].compareTo(in.getAddress()) < 0) back++;
            }
            if (and15 > 0 && sh4 > 0 && back > 0)
                println(String.format("%s %d and15=%d sh4=%d back=%d", f.getName(), len, and15, sh4, back));
        }
    }
}
