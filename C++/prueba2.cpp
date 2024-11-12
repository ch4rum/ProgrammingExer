#include <iostream>
#include <unistd.h>

int main(){

    write(1, "Hola, mundo!\n", 13);
    return 0;
}