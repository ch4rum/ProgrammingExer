
public class NodoStringPhrase {

    /**
     * Representacion de la lista doblemente enlazada que almacena cadenas de texto, 
     * cada nodo almacena una frase.
     * 
     * Atributos: 
     * - phrase: Representa la frase almacenada en el nodo.
     * - prev: Referencia/Puntero al nodo anterior.
     * - next: Referencia/Puntero al nodo siguiente.
     * 
     * Constructores:
     * - NodoStringPhrase: Hay definidos dos constructores uno cuando NO hay datos en 
     * el la lista y otro cuando SI hay datos en la lista.
     */

    public String phrase;
    public NodoStringPhrase prev, next;

    // Constructor when there is no data
    public NodoStringPhrase(String dataphrase){
        this(dataphrase, null, null);
    }

    // Constructor when there is data
    public NodoStringPhrase(String dataphrase, NodoStringPhrase ps, NodoStringPhrase pa){
        phrase = dataphrase;
        next = ps;
        prev = pa;
    }

}
