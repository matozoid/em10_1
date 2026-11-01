// For each defined string containing a given substring (script args), print address, text, and referencing functions.
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.*;
import ghidra.program.model.symbol.*;
import ghidra.program.model.address.Address;

public class StringXrefs extends GhidraScript {
    @Override
    protected void run() throws Exception {
        String[] pats = getScriptArgs();
        for (Data d : currentProgram.getListing().getDefinedData(true)) {
            Object v = d.getValue();
            if (!(v instanceof String)) continue;
            String s = (String) v;
            for (String p : pats) {
                if (!s.contains(p)) continue;
                StringBuilder sb = new StringBuilder();
                for (Reference r : getReferencesTo(d.getAddress())) {
                    Function f = getFunctionContaining(r.getFromAddress());
                    sb.append(" ").append(r.getFromAddress()).append(f != null ? "(" + f.getName() + ")" : "");
                }
                println(d.getAddress() + " \"" + s + "\" <-" + sb);
                break;
            }
        }
    }
}
