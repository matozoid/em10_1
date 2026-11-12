// Apply documented symbol names to the program. arg0 = TSV from `tools/symbols.py export`
// (address <TAB> name <TAB> file), arg1 = "dry" to only count.
// A function at the address is renamed; an address without a function gets a label. Names already equal
// are skipped. Run WITHOUT -readOnly, e.g.:
//   analyzeHeadless research/ghidra_proj em10 -process blk00_40300000.bin -noanalysis \
//     -scriptPath tools/ghidra -postScript ApplyNames.java /path/to/names.tsv
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.symbol.SourceType;
import java.io.BufferedReader;
import java.io.FileReader;

public class ApplyNames extends GhidraScript {
    @Override
    protected void run() throws Exception {
        String[] args = getScriptArgs();
        boolean dry = args.length > 1 && args[1].equals("dry");
        int renamed = 0, same = 0, labels = 0, failed = 0;
        try (BufferedReader r = new BufferedReader(new FileReader(args[0]))) {
            String line;
            while ((line = r.readLine()) != null) {
                String[] p = line.split("\t");
                if (p.length < 2 || p[1].isEmpty()) continue;
                String name = p[1].replace(':', '_').replace('+', '_');
                Address a;
                try {
                    a = toAddr(Long.parseLong(p[0], 16));
                } catch (NumberFormatException e) { failed++; continue; }
                if (!currentProgram.getMemory().contains(a)) { failed++; continue; }
                Function f = getFunctionAt(a);
                try {
                    if (f != null) {
                        if (f.getName().equals(name)) { same++; continue; }
                        if (!dry) f.setName(name, SourceType.USER_DEFINED);
                        renamed++;
                    } else {
                        if (!dry) createLabel(a, name, true, SourceType.USER_DEFINED);
                        labels++;
                    }
                } catch (Exception e) {
                    failed++;
                    println("failed " + p[0] + " " + name + ": " + e.getMessage());
                }
            }
        }
        println(String.format("%sfunctions renamed: %d, already named: %d, labels created: %d, failed or outside memory: %d",
            dry ? "[dry run] " : "", renamed, same, labels, failed));
    }
}
