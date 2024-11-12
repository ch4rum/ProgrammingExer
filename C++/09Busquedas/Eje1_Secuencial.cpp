#include <iostream>

// O(n)
int main(){
    int numbers[] = {2,4,5,1,6,3}, count = 0, date;
    bool key = true;

    std::printf("Ingrese un numero: ");
    std::cin>>date;
    
    // Busqueda secuencial
    while ( (key) && (count<sizeof numbers/sizeof numbers[0]) ){
        if (numbers[count] == date){
            key = false;
            break;
        }
        count++;
    }
    if (!key){
        std::printf("El numero se encontro en la posicion %d.\n",count);
    } else {
        std::printf("No se encontro el numero en el arreglo.\n");
    }
    return 0;
}