#include <iostream>
#include <cstring>

int main() {
    char key[] = "oso";
    char user[80];
    std::string attempt;
    do {
        std::printf("\nCual es mi animal?: ");
        std::cin >> user;
        if (std::strcmp(key, user) != 0) {
            std::printf("\nPrueba otro\n");
        } else if (std::strcmp(key, user) == 0) {
            std::printf("\nCorrecto!...\n");
        }
    } while (std::strcmp(key, user) != 0);
    std::printf("\nIngrese una cadena: ");
    std::cin>>attempt;

    std::printf("La longitud de la cadena es: %lld\n",attempt.length());

    if ( (!std::isdigit(key[0])) || (!std::isdigit(key[1])) || (!std::isdigit(key[2])) ) {
        std::printf("El primer carácter es un dígito.\n");
        std::printf("La clave tiene: %lld digitos\n",strlen(key));
    }

    return 0;
}