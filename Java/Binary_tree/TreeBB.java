
public class TreeBB{
  
  /**
   * Representacion del árbol binario de busqueda, donde cada nodo tiene como máximo dos hijos,
   * un hijo izquierdo y un hijo derecho, para cada nodo del árbol, los valores alamacenados
   * en el subárbol izquierdo son menores que el valor almacenado en el nodo, y los valores en
   * el subárbol derecho son mayores.
   * 
   * Atributos:
   * - root: Referencia/Puntero a la raíz del árbol.
   * 
   * Constructor:
   * - TreeBB: Inicializa un árbol binario de búsqueda vacío.
   * 
   * Métodos públicos:
   * - insert(int value): Inserta un valor en el árbol.
   * - itsempty(): Verifica si el árbol está vacío.
   * - preordenTree(StringBuilder List): Realiza un recorrido en preorden y almacena los valores en una cadena
   * - inordenTree(StringBuilder List): Realiza un recorrido en inorden y almacena los valores en una cadena
   * - posordenTree(StringBuilder List): Realiza un recorrido en posorden y almacena los valores en una cadena
   * - search(int date): Busca un valor en el árbol y devuelve falso sino está y true si está presente.
   * - remove(int date): Elimina un valor del árbol
   * 
   * Métodos privados:
   * - inserRec(Node father, int val): Auxiliar para la inserción recursiva.
   * - preordenTree(Node n,StringBuilder list): Auxiliar para el recorrido preorden recursivo.
   * - inordenTree(Node n,StringBuilder list): Auxiliar para el recorrido inorden recursivo.
   * - posordenTree(Node n,StringBuilder list): Auxiliar para el recorrido posorden recursivo.
   * - search(Node father, int val): Auxiliar para la bsqueda recursiva de un valor.
   * - remove(Node father, int date): Auxiliar para eliminar unv alor del árbol recuisivo.
   * - minValues(Node father): Auxiliar para encontrar el valor mínimo en un subárbol.
   */

  private Node root;

  // Builder
  TreeBB() {
    this.root = null;
  }

  // Method public for insert values
  void insert(int value){
    root = insertRec(root, value);
  }

  // Private methos that inserts values recursively
  private Node insertRec(Node father, int val){
    if (father == null){
      return new Node(val);
    }
    if (val > father.getDate()){
      if (father.getSonDer() == null){
        father.setSonDer(new Node(val));
      } else {
        this.insertRec(father.getSonDer(), val);
      }
    } else if (val < father.getDate()){
      if(father.getSonIzq() == null){
        father.setSonIzq(new Node(val));
      } else{
        this.insertRec(father.getSonIzq(), val);
      }
    }
    return father;
  } 

  // Method it's empty
  boolean itsempty(){
    return this.root==null;
  }

  // Method to display preorden
  void preordenTree(StringBuilder list){
    preordenTree(this.root, list);
  }

  // Method recursive for preorden
  private void preordenTree(Node n, StringBuilder list){
    if (n != null){
      list.append(n.getDate()).append(" ");
      preordenTree(n.getSonIzq(),list);
      preordenTree(n.getSonDer(),list);
    }
  }

  // Method to display inorden
  void inordenTree(StringBuilder list){
    inordenTree(this.root, list);
  }

  // Method recursive for inorden
  private void inordenTree(Node n, StringBuilder list){
    if(n != null){
      inordenTree(n.getSonIzq(),list);
      list.append(n.getDate()).append(" ");
      inordenTree(n.getSonDer(),list);
    }
  }

  // Metho to display posorden
  void posordenTree(StringBuilder list){
    posordenTree(this.root, list);
  }

  // Method recursive for posorden
  private void posordenTree(Node n, StringBuilder list){
    if(n != null){
      posordenTree(n.getSonIzq(),list);
      posordenTree(n.getSonDer(),list);
      list.append(n.getDate()).append(" ");
    }
  }

  // Method to find a node
  boolean search(int date){
    return search(this.root, date);
  }

  // Method recursive to find a node
  private boolean search(Node father, int val){
    if (father == null || father.getDate() == val){
      return father != null;
    }

    if (val < father.getDate()){
      return search(father.getSonIzq(),val);
    }
    return search(father.getSonDer(),val);
  }

  // Method for delete node
  void remove(int date){
    root = remove(this.root, date);
  }

  // Method recursive to delete node
  private Node remove(Node father, int date){
    if (father == null){
      return father;
    }
    if (date < father.getDate()){
      father.setSonIzq(remove(father.getSonIzq(), date));
    } else if (date > father.getDate()){
      father.setSonDer(remove(father.getSonDer(), date));
    } else {
      if (father.getSonIzq() == null){
        return father.getSonDer();
      } else if (father.getSonDer() == null){
        return father.getSonIzq();
      }
      father.setDate(minValues(father.getSonDer()));
      father.setSonDer(remove(father.getSonDer(), father.getDate()));
    }
    return father;
  }

  // Method helper of remove, find the minimum value
  private int minValues(Node father){
    Node val = father.getSonDer();
    Node prev = null;
    while (val.getSonIzq() != null){
      prev = val;
      val = val.getSonIzq();
    }
    if (prev != null){
      prev.setSonIzq(val.getSonDer());
      val.setSonDer(father.getSonDer());
    }
    return val.getDate();
  }
}
