// Disassemble N bytes at each address given as script args (hex) and print listing.
// usage: analyzeHeadless ... -postScript DisasAt.java 0x403001ab 64 ...
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Instruction;

public class DisasAt extends GhidraScript {
    @Override
    protected void run() throws Exception {
        String[] a = getScriptArgs();
        for (int i = 0; i + 1 < a.length; i += 2) {
            Address s = toAddr(Long.decode(a[i]));
            int n = Integer.decode(a[i + 1]);
            clearListing(s, s.add(n));
            disassemble(s);
            println("== " + s);
            Address p = s;
            while (p.compareTo(s.add(n)) < 0) {
                Instruction in = getInstructionAt(p);
                if (in == null) { println(p + ": ?? " + String.format("%02x", getByte(p) & 0xff)); p = p.add(1); continue; }
                println(p + ": " + in);
                p = p.add(in.getLength());
            }
        }
    }
}
