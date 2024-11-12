#include <iostream>
#include <limits>

struct Direction_info{
    char direction[30];
    char city[20];
    char provi[20];
};

struct Person{
    char name[30];
    struct Direction_info dir_empleado;
    double cash;
}empleado[2];

int main (){

    for(int _=0;_<2;_++){
        printf("Nombre: ");std::cin.getline(empleado[_].name,30,'\n');
        printf("Direccion: ");std::cin.getline(empleado[_].dir_empleado.direction,30,'\n');
        printf("Ciudad: ");std::cin.getline(empleado[_].dir_empleado.city,30,'\n');
        printf("Provincia: ");std::cin.getline(empleado[_].dir_empleado.provi,30,'\n');
        printf("Salario: ");std::cin>>empleado[_].cash;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Limpia el búfer después de leer el salario
        printf("\n");
    }
    for(int _=0;_<2;_++){
        printf("\nNombre: %s\n",empleado[_].name);
        printf("Direccion: %s\n",empleado[_].dir_empleado.direction);
        printf("Ciudad: %s\n",empleado[_].dir_empleado.city);
        printf("Provincia: %s\n",empleado[_].dir_empleado.provi);
        printf("Salario: %f\n",empleado[_].cash);
        printf("\n");
    }

    return 0;
}