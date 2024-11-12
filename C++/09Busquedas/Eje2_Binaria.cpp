#include <iostream>
// O(log_2 N)
int main(){ 
    int numbers [] = {3,7,10,23,45};
    int inf = 0, supe, mitad, date;
    bool key = true;

    std::printf("Ingrese un numero: ");
    std::cin>>date;

    supe = sizeof numbers/sizeof numbers[0];
    
    // Busqueda Binaria
    while( (inf <= supe) && (key) ){
        mitad = (inf+supe)/2;
        if (numbers[mitad] == date){
            key = false; break;
        }else if (numbers[mitad] > date){
            supe = mitad - 1;
        }else if (numbers[mitad] < date){
            inf = mitad + 1;
        }
    }
    if (!key){
        std::printf("El numero se encontro en la posicion %d.\n",mitad);
    } else {
        std::printf("El numero no ha sido encontrado.\n");
    }
    return 0;
}