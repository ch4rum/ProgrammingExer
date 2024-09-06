import javax.swing.JOptionPane;

public class Binary_tree{

  /**
   * Main del programa con menus interactivos, para representar cada opcion de un árbol binario
   * de busqueda.
   * 
   * Métodos:
   * - main(String[] args): Este es el método iprincipal del programa
   * - MenuManager(TreeBB tree): Gestiona el menú principal del programa
   * - handler_options(int Option, TreeBB tree): Maneja las diferentes opciones del ménu principal
   * - submenu(TreeBB tree): Muestra un submenu para imprimir los nodos.
   * - sub_handler_options(int Option, TreeBB tree): Maneja las opciones que trae el submenú imprimir. 
   */

   // Method main
  public static void main(String[] args) {
    TreeBB tree = new TreeBB();
    MenuManager(tree);
  }

  // Builder menu
  private static void MenuManager(TreeBB tree) {
    int Option = 0;
    do{
      try{
        Option = Integer.parseInt(JOptionPane.showInputDialog(null,
        "                 .: Menu :.\n"
        +"1. Agregar un elemento(Nodo)\n"
        + "2. Imprimir elementos\n"
        + "3. Borrar elementos\n"
        + "4. Salir\n"
        + "\nElige Una Opción..","Árboles Binarios", JOptionPane.QUESTION_MESSAGE));
        handler_options(Option, tree);
      }catch(NumberFormatException n){
        JOptionPane.showMessageDialog(null, "[x] ERROR: "+ n,"Error",
        JOptionPane.ERROR_MESSAGE);
      }
    }while(Option !=4);
  }

  // Method that handles menu options
  private static void handler_options(int Option, TreeBB tree){
    int element;
    switch (Option) {
      case 1:
        element = Integer.parseInt(JOptionPane.showInputDialog(null,
        "Ingrese el numero del Nodo", "Agregando Nodo",
        JOptionPane.QUESTION_MESSAGE));
        tree.insert(element);
        break;
      case 2:
        submenu(tree);
        break;
      case 3:
        if (!tree.itsempty()){
          element = Integer.parseInt(JOptionPane.showInputDialog(null,
          "Ingrese el numero del Nodo ha eliminar", "Eliminando Nodo",
          JOptionPane.QUESTION_MESSAGE));
          if (tree.search(element)){
            tree.remove(element);
            JOptionPane.showMessageDialog(null, "Se ha eliminado el nodo con éxito","Eliminando Nodo",
            JOptionPane.INFORMATION_MESSAGE);
          } else{
            JOptionPane.showMessageDialog(null,"No se ha encontrado el nodo para eliminar","!Cuidado",
            JOptionPane.ERROR_MESSAGE);
          }
        } else {
          JOptionPane.showMessageDialog(null, "El Árbol está vacío", "!Cuidado",
          JOptionPane.ERROR_MESSAGE);
        }
        break;
      case 4:
        JOptionPane.showMessageDialog(null, "Aplicacion Finalizada","Fin",
        JOptionPane.INFORMATION_MESSAGE);
        break;
      default:
        JOptionPane.showMessageDialog(null, "[!] Seleccione una opción correcta","Cuidado",
        JOptionPane.INFORMATION_MESSAGE);
        break;
    }
  }

  // Method that manages the submenu
  private static void submenu(TreeBB tree){
    int Option = 0;
      try{
        Option = Integer.parseInt(JOptionPane.showInputDialog(null,
        "                 .: Imprimir :.\n"
        +"1. Inorden\n"
        + "2. PosOrden\n"
        + "3. PreOrden\n"
        + "\nElige Una Opción..","Imprimir Datos", JOptionPane.QUESTION_MESSAGE));
        sub_handler_options(Option, tree);
      }catch(NumberFormatException n){
        JOptionPane.showMessageDialog(null, "[x] ERROR: "+ n,"Error",
        JOptionPane.ERROR_MESSAGE);
      }
  }

  // Method that handles submenu options
  private static void sub_handler_options(int Option, TreeBB tree){
    StringBuilder elements = new StringBuilder();
    switch (Option) {
      case 1:
        if (!tree.itsempty()){
          tree.inordenTree(elements);
          JOptionPane.showMessageDialog(null,"Elementos del Arbol (InOrden): "+elements.toString(),
          "Arbol", JOptionPane.INFORMATION_MESSAGE);
        } else {
          JOptionPane.showMessageDialog(null, "El Árbol está vacío", "!Cuidado",
          JOptionPane.ERROR_MESSAGE);
        }
        break;
      case 2:
        if (!tree.itsempty()){
          tree.posordenTree(elements);
          JOptionPane.showMessageDialog(null,"Elementos del Arbol (PosOrden): "+elements.toString(),
          "Arbol", JOptionPane.INFORMATION_MESSAGE);
        } else {
          JOptionPane.showMessageDialog(null, "El Árbol está vacío", "!Cuidado",
          JOptionPane.ERROR_MESSAGE);
        }
        break;
      case 3:
        if (!tree.itsempty()){
          tree.preordenTree(elements);
          JOptionPane.showMessageDialog(null,"Elementos del Arbol (PreOrden): "+elements.toString(),
          "Arbol", JOptionPane.INFORMATION_MESSAGE);
        } else {
          JOptionPane.showMessageDialog(null, "El Árbol está vacío", "!Cuidado",
          JOptionPane.ERROR_MESSAGE);
        }
        break;
      default:
        JOptionPane.showMessageDialog(null, "[!] Seleccione una opción correcta","Cuidado",
        JOptionPane.INFORMATION_MESSAGE);
        break;
    }
  }
}
