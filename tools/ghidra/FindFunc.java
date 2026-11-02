// Print address of functions whose name contains any arg substring.
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;

public class FindFunc extends GhidraScript {
    public void run() throws Exception {
        String[] args = getScriptArgs();
        Function f = getFirstFunction();
        while (f != null) {
            String n = f.getName();
            for (String a : args) {
                if (n.contains(a)) {
                    println(f.getEntryPoint() + "\t" + n);
                    break;
                }
            }
            f = getFunctionAfter(f);
        }
    }
}
