// Histogram of 32-bit scalar operands in code, bucketed by 1 MB (arg0 = min bucket count to print).
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.*;
import ghidra.program.model.scalar.Scalar;
import java.util.*;

public class ImmHist extends GhidraScript {
    @Override
    protected void run() throws Exception {
        TreeMap<Long, Integer> h = new TreeMap<>();
        for (Instruction in : currentProgram.getListing().getInstructions(true)) {
            for (int i = 0; i < in.getNumOperands(); i++) {
                for (Object o : in.getOpObjects(i)) {
                    if (o instanceof Scalar) {
                        long v = ((Scalar) o).getUnsignedValue();
                        if (v >= 0x01000000L && v < 0x100000000L) h.merge(v >> 20, 1, Integer::sum);
                    }
                }
            }
        }
        int min = Integer.parseInt(getScriptArgs()[0]);
        for (Map.Entry<Long, Integer> e : h.entrySet())
            if (e.getValue() >= min) println(String.format("%08x %d", e.getKey() << 20, e.getValue()));
    }
}
