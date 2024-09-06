import java.io.IOException;

public class OutputInScreen {

    /**
     * Esta clase proporciona metodos para realizar operaciones relacionadas con la salida
     * en pantalla como borrar la pantalla y pausar la ejecucion.
     * 
     * Metodos:
     * - clear: Borra la pantalla de la consola, utilizando el comando 'cls' en windows y 'clear' en otros OS.
     * - isOS: Comprueba si el OS actual es windows, retorna true o false.
     * - sleep: Duerme o pausa, la ejecucion del programa durante un tiempo en milisegundos.
     */

    // Clear Screen in OS
    public void clear(){
        try {
            if (isOS()){
                new ProcessBuilder("cmd","/c","cls").inheritIO().start().waitFor();
            } else {
                new ProcessBuilder("clear").inheritIO().start().waitFor();
            }
        } catch (IOException | InterruptedException e){
            e.printStackTrace();
        }
    }

    // which OS
    private static boolean isOS(){
        return System.getProperty("os.name").toLowerCase().contains("windows");
    }
    
    // Thread sleep time
    public void sleep(int time){
        try {
            Thread.sleep(time);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
