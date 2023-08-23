/* 9. Realice un programa que lea una cadena de la entrada y muestre en la 
salida estadar cuantas ocurrencias de cada vocal existe en la cadena*/

#include <iostream>
#include <cstring>

using namespace std;

int main(){
    char phrase[100];
    int vowel_a=0, vowel_e=0, vowel_i=0, vowel_o=0, vowel_u=0;
    int lengthOne;

    do {
        cout<<"Digite una cadena de caracteres: ";
        cin.getline(phrase,100,'\n');
        lengthOne = strlen(phrase);    
    } while ( lengthOne == 0);

    for (int _=0; _<lengthOne; _++){
        switch(phrase[_]){
            case 'a':vowel_a++;break;
            case 'e':vowel_e++;break;
            case 'i':vowel_i++;break;
            case 'o':vowel_o++;break;
            case 'u':vowel_u++;break;
        }
    }
    cout<<"Vocal a: "<<vowel_a<<endl;
    cout<<"Vocal e: "<<vowel_e<<endl;
    cout<<"Vocal i: "<<vowel_i<<endl;
    cout<<"Vocal o: "<<vowel_o<<endl;
    cout<<"Vocal u: "<<vowel_u<<endl;

    return 0;
}