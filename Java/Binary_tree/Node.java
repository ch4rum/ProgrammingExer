public class Node{

  /**
   * Representación de un nodo en una estructura de árbol binario, donde cada nodo
   * almacena un entero.
   * 
   * Atributos:
   * - date: Representa el entero alamacenado en el nodo.
   * - SonIzq: Referencia/Puntero al hijo izquierdo del nodo.
   * - SonDer: Referencia/Puntero al hijo dereccho del nodo.
   * 
   * Constructor:
   * - Node: Se define un constructor que recibe un numero, y inicializa los atributos.
   * 
   * Métodos:
   * - getDate(): Devuelve el entero almacenado en el nodo.
   * - setDate(int d): Establece el entero alamacenado en el nodo.
   * - getSonDer(): Devuelve una referencia al hijo derecho del nodo.
   * - setSonDer(Node der): Establece el hijo derecho del nodo.
   * - getSonIzq(): Devuelve una referencia al hijo izquierdo del nodo.
   * - setSonIzq(Node izq): Establece el hijo izquierdo del nodo.
   */

  private int date;
  private Node SonIzq;
  private Node SonDer;
  
  // Builder
  Node(int d){
    this.date = d;
    this.SonIzq = this.SonDer = null;
  }

  int getDate(){
    return this.date;
  }

  void setDate(int d){
    this.date = d;
  }

  Node getSonDer(){
    return SonDer;
  }

  void setSonDer(Node der){
    this.SonDer = der;
  }

  Node getSonIzq(){
    return SonIzq;
  }

  void setSonIzq(Node izq){
    this.SonIzq = izq;
  }
}
