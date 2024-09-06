import java.util.InputMismatchException;
import java.util.Scanner;

public class MenuManager {
    
    /**
     * Esta clase representa el menu para probar cada opcion de la lista doblemente enlazada.
     * 
     * Atributos: 
     * - output: Manejador para borrar la pantalla y pausar la ejecucion unos segundos a lo largo de la clase.
     * - list: Lista doblemente enlazada donde se guardaran las frases.
     * - data: Scanner encargado de recibir el input del usuario.
     * 
     * Contructor:
     * - MenuManager: Contructor que inicializa los atributos.
     * 
     * Metodos:
     * - menu: Muestra el menu con todas sus opciones y maneja la interaccion con el usuario.
     * - handler_options: Maneja las opciones del menu segun la digitada por el usuario.
     * - Inputposition: Solicita una posicion y gestiona si el dato ingresado es un numero entero valido.
     * - InputPhrase: Gestiona el ingreso de una frase.
     */

    private OutputInScreen output;
    private PhraseListDouble list;
    private Scanner data;

    // Builder
    public MenuManager(){
        output = new OutputInScreen();
        list = new PhraseListDouble();
        data = new Scanner(System.in);
        this.menu();
    }
    
    // Method show menu and manager options
    private void menu(){
        int Option = 0;
        do{
            try {
                output.clear();
                System.out.println("\n\t.: MENU :.\n\n1) Ingresar una frase.\n"
                    + "2) Mostrar frase de una posicion de la lista.\n"
                    + "3) Comprobar si una frase esta en la lista.\n"
                    + "4) Imprimir frases de la lista.\n"
                    + "5) Numero de frases en la lista.\n"
                    + "6) Sacar una frase de la lista.\n"
                    + "7) Sacar frase de una pocion de la lista.\n"
                    + "8) Concatenar dos listas.\n"
                    + "9) Reemplazar un frase de la lista.\n"
                    + "10) Exit.");
                System.out.print("\n[+] Opcion :> ");
                Option = data.nextInt();
                handler_options(Option, data);
            } catch (InputMismatchException n) {
                System.out.println("\n[x] Error: Ingrese un numero entero valido");
                data.next();
                output.sleep(1500);
            }
        } while (Option != 10);
        data.close();
    }
    
    // Method to handle menu options.
    private void handler_options (int number, Scanner pause){
        switch (number) {
            case 5:
                output.clear();
                System.out.println("\n\t.: Numero de elementos :.");
                System.out.println("\n[+] El numero de elementos en la lista es: " + list.getSize());
                pause.nextLine();
                System.out.print("\nPresiona <ENTER> para continuar");
                pause.nextLine();
                break;
            case 2:
                output.clear();
                System.out.println("\n\t.:  Mostrar frase de una pocision :.");
                list.whatPosition(InputPosition(pause));
                pause.nextLine();
                System.out.print("\nPresiona <ENTER> para continuar");
                pause.nextLine();
                break;
            case 3:
                output.clear();
                System.out.println("\n\t.: Comprobar si la frase esta en la lista :.");
                list.isOnList(InputPhrase(pause,3));
                System.out.print("\nPresiona <ENTER> para continuar");
                pause.nextLine();
                break;
            case 4:
                output.clear();
                System.out.println("\n\t.: Elementos de la lista :.\n");
                list.showListStartEnd();
                System.out.print("\nPresiona <ENTER> para continuar");
                pause.nextLine();
                pause.nextLine();
                break;
            case 1:
                output.clear();
                System.out.println("\n\t.: Insertar una frase :.");
                list.appendEnd(InputPhrase(pause,5));
                System.out.print("\nPresiona <ENTER> para continuar");
                pause.nextLine();
                break;
            case 6:
                output.clear();
                System.out.println("\n\t.: Sacar una frase :.");
                list.removePhrase(InputPhrase(pause, 6));
                System.out.print("\nPresiona <ENTER> para continuar");
                pause.nextLine();
                break;
            case 7:
                output.clear();
                System.out.println("\n\t.: Sacar frase de una pocision :.");
                list.removePhrasePosition(InputPosition(pause));;
                pause.nextLine();
                System.out.print("\nPresiona <ENTER> para continuar");
                pause.nextLine();
                break;
            case 8:
                output.clear();
                System.out.println("\n\t.: Unir dos listas :.");
                PhraseListDouble twoList = new PhraseListDouble();
                twoList.appendEnd(InputPhrase(pause, 8));
                list.extendList(twoList);
                System.out.print("\nPresiona <ENTER> para continuar");
                pause.nextLine();
                break;
            case 9:
                output.clear();
                System.out.println("\n\t.: Remplazar una frase :.");
                int position = InputPosition(pause);
                list.replaceList(position, InputPhrase(pause, 9));
                System.out.print("\nPresiona <ENTER> para continuar");
                pause.nextLine();
                break;
            case 10:
                System.out.println("\n...Saliendo del programa...\n");
                pause.close();
                break;
            default:
                System.out.println("\n[!] Seleccione una opción correcta.");
                output.sleep(1500);
                break;
        }
    }
    
    // Case two, seven
    private int InputPosition(Scanner save){
        while (true){
            try{
                System.out.print("\nInserte la posión:> ");
                int number = save.nextInt();
                return number;
            } catch (InputMismatchException n) {
                System.out.println("\n[x] Error: Ingrese un numero entero valido");
                save.nextLine();
            }
        }
    }

    // Case one, three, six, eight, nine
    private String InputPhrase(Scanner save, int casen){
        save.nextLine();
        System.out.print("\nInserte la frase:> ");
        String phrase = save.nextLine();
        switch (casen) {
            case 5:
                System.out.println("\n[+] Frase '"+ phrase+"' agregada exitosamente");
                break;
            case 8:
                System.out.println("\n[+] Frase '"+ phrase+"' agregada exitosamente a la segunda lista.");
                break;
        }
        return phrase;
    }

}
