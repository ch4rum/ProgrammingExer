package Lab_Credit;

import java.util.HashMap;
import java.util.Map;

public class WriteOutput {

    private static final String RESET = "\033[0m";  // Reset colour
    private static final String GREEN = "\033[32m"; // Verde
    private static final String BLUE = "\033[34m";  // Azul
    private static final String RED = "\033[31m";   // Rojo
    private static final String YELLOW = "\033[33m"; // Amarillo

    private Map<String, String> errorMap;

    public WriteOutput() {
        errorMap = new HashMap<>();
        errorMap.put("OK", GREEN + "[+] " + RESET);
        errorMap.put("FAILED", BLUE + "[x] FAILED: ");
        errorMap.put("ERROR", RED + "[-] ERROR: " );
        errorMap.put("WARNING", YELLOW + "[!] WARNING: ");
        errorMap.put(" ", "");
    }

    public void printDebug(String type_error, String message){
        String prefix = errorMap.getOrDefault(type_error, "");
        System.out.println(prefix + message + RESET);
    }

    public void printDebug(String type_error, String message, String end) {
        String prefix = errorMap.getOrDefault(type_error, "");
        System.out.print(prefix + message + RESET + end);
    }

    public String getRESET(){
        return this.RESET;
    }

    public String getGREEN(){
        return this.GREEN;
    }

    public String getBLUE(){
        return this.BLUE;
    }
}