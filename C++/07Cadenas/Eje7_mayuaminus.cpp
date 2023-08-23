/* 7, Pedir su nombre al usuario en mayusculas, si su nombre comienza
por la letra A convertir su nombre a minusculas, caso contrario no convertirlo*/

#include <iostream>
#include <cstring>
#include <cctype>

using namespace std;

int main(){
    char username[100];
    int lengthOne;

    do {
        cout<<"Digite su nombre en mayusculas: ";
        cin.getline(username,100,'\n');
        lengthOne = strlen(username);
    } while (lengthOne == 0);

    if (username[0] == 'A'){
        for(int _=0;_<lengthOne;_++){
            username[_] = tolower(username[_]);
        }
        cout<<username<<endl;
    } else {
        cout<<username<<endl;
    }
    return 0;
}