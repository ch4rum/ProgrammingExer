package Lab_Credit;

import java.io.IOException;

public class Output{

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
