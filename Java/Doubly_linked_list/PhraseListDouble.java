
public class PhraseListDouble {

    /**
     * Clase que representa una lista doblemente enlazada de frases, permite realizar 
     * diversas operaciones.
     * 
     * Atributos:
     * - start: Primer nodo de la lista.
     * - end: Ultimo nodo de la lista.
     * - size: Tamaño actual de la lista.
     * 
     * Contructor:
     * - PhraseListDouble: Contructor que inicializa una lista doblemente enlazada vacia.
     * 
     * Metodos:
     * - itsempty: Verifica si la lista esta vacia.
     * - getSize: Obtiene  el tamaño actual de la lista.
     * - whatPosition: Muestra la frase en una posicion especifiaca de la lista.
     * - isOnList: Verifica si una frase esta presente en la lista.
     * - showListStartEnd: Muestra todas las frase en la lista de principio a fin.
     * - appendEnd: Agrega una frase al final de la lista.
     * - appendStart: Agrega una frase al principio de la lista.
     * - removePhrase: Elimina una frase especifica de la lista.
     * - removePhrasePosition: ELimina la frase en una posicion especifica de la lista.
     * - extendList: Extiende la lista actual concatenandola con otra lista.
     * - replaceList: Reemplaza una frase en una posicion especifica de la lista.
     */

    private NodoStringPhrase start, end;
    private int size = 0;

    public PhraseListDouble(){
        start = end = null;
    }

    // Method it's empty
    public boolean itsempty(){
        return start == null;
    }

    // Method size list
    public int getSize(){
        return size;
    }

    // Method to get an phrase at a specific position
    public void whatPosition(int index){
        if (!itsempty()){
            if (index <0 || index >= size){
                System.out.println("\n[!] Indice fuera de rango");
            } else {
                NodoStringPhrase current = start;
                for (int i=0; i<index;i++){
                    current = current.next;
                }
                System.out.println("\n[+] La frase en la posicion " + index + " es: " + current.phrase);
            }
        } else {
            System.out.println("\n[!] La lista esta vacia.");
        }
    }

    // Is on list
    public void isOnList(String data){
        NodoStringPhrase phrase = start;
        boolean flag = false;
        while (phrase != null){
            if (phrase.phrase.equals(data)){
                flag = true;
                break;
            }
            phrase = phrase.next;
        }
        if (flag){
            System.out.println("\n[+] La frase '" + data + "' si esta en la lista.");
        } else {
            System.out.println("\n[!] La frase '" + data + "' no esta en la lista.");
        }
    }
    // Method to display the list from start to end
    public void showListStartEnd(){
        if(!itsempty()){
            NodoStringPhrase aux = start;
            while (aux != null){
                System.out.println("* "+ aux.phrase+".");
                aux = aux.next;
            }
        } else {
            System.out.println("[!] No se ha agregado ninguna frase.");
        }
    }

    // Method for append nodes to the end
    public void appendEnd(String data){
        if(!itsempty()){
            end = new NodoStringPhrase(data, null, end);
            end.prev.next = end;
            size++;
        } else {
            start = end = new NodoStringPhrase(data);
            size++;
        }
    }

    // Method for append nodes to the start
    public void appendStart(String data){
        if(!itsempty()){
            start = new NodoStringPhrase(data, start, null);
            start.next.prev = start;
            size++;
        } else {
            start = end = new NodoStringPhrase(data);
            size++;
        }
    }

    // Method remove of list
    public void removePhrase(String data){
        if (!itsempty()){
            NodoStringPhrase current = start;
            while (current != null){
                if (current.phrase.equals(data)){
                    if (current == start){ // at the beginning
                        start = current.next;
                        if (start != null){
                            start.prev = null;
                        } else {
                            end = null;
                        }
                    } else if (current == end){ // in the end
                        end = end.prev;
                        end.next = null;
                    } else { // in the middle
                        current.prev.next = current.next;
                        current.next.prev = current.prev;
                    }
                    size--;
                    System.out.println("\n[+] Se ha eliminado la frase.");
                    return;
                }
                current = current.next;
            }
            System.out.println("\n[!] La frase no esta en la lista.");
        } else {
            System.out.println("\n[!] La lista esta vacia. No se puede eliminar la frase.");
        }
    }

    // Method remove of list position
    public void removePhrasePosition(int index){
        if (!itsempty()){
            if (index < 0 || index >= size){
                System.out.println("\n[!] Indice fuera de rango");
            } else {
                NodoStringPhrase current = start;
                for (int i=0; i<index;i++){
                    current = current.next;
                }
                if (current == start){ // at the beginning
                    start = current.next;
                    if (start != null){
                        start.prev = null;
                    } else {
                        end = null;
                    }
                } else if (current == end){ // in the end
                    end = end.prev;
                    end.next = null;
                } else { // in the middle
                    current.prev.next = current.next;
                    current.next.prev = current.prev;
                }
                size--;
                System.out.println("\n[+] Se ha eliminado la frase.");
            }
        } else {
            System.out.println("\n[!] La lista esta vacia, nose puede eliminar.");
        }
    }

    // Method extend list
    public void extendList(PhraseListDouble listTwo){
        if (!listTwo.itsempty()){
            if (itsempty()){
                start = listTwo.start;
                end = listTwo.end;
            } else {
                end.next = listTwo.start;
                listTwo.start.prev = end;
                end = listTwo.end;
            }
            size += listTwo.size;
            System.out.println("\n[+] Se han unido las dos lista exitosamente.");
        } else {
            System.out.println("\n[!] La segunda lista esta vacia, nose puden concatenar.");
        }
    }

    // Method replace in list
    public void replaceList(int index, String data){
        NodoStringPhrase current = start;
        if (!itsempty()){
            if (index < 0 || index >= size){
                System.out.println("\n[!] Indice fuera de rango. No se puede remplazar la frase.");
            } else {
                for (int i=0; i<index;i++){
                    current = current.next;
                }
                current.phrase = data;
                System.out.println("\n[+] La frase se ha remplazado exitosamente.");
            }
        } else {
            System.out.println("\n[!] No se puede remplazar porque la lista esta vacia.");
        }
    }
}
