/*         
                         #                        
                       @@@@#                      
                     %@@@@@@@                     
                    @@@@@@@@@@@                   
                  @@@@@@@@@@@@@@#                
                @@@@@@@@@@@@@@@@@@.               
              &@@@@@@@@@@@@@@@@@@@@@              
            @@@@@@@@@@@@@@@@@@@@@@@@@@            
           @@/       \@@@@@@@/       \@@          ~ ch4rum
         @@@@    __   \@@@@@@    _____|@@@        ~ https://github.com/ch4rum/ProgrammingExer
        @@@@@   |@@|  |@@@@@@   |@@@@@@@@@@       ~ python3
      %@@@@@@   ---   |@@@@@@      \@@@@@@@@      
      @@@@@@@    ____/@@@@@@@    __|@@@@@@@@@     
     .@@@@@@@   |@@@@@@@@@@@@   |@@@@@@@@@@@@     
      @@@@@@@   |@@@@@ @ @@@@   |@@@@@@@@@@@@     
       @@@@@@\__|@@@@  @ @@@@\__|@@@@@@@@@@.      
         @@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@        
                    @@@@@@@@@@@                   
                   @@@@@@@@@@@@@                  
                  @@@@@@@@@@@@@@@                 
*/

#include<iostream>
#include<stdlib.h>
#include<time.h>
#include<string>
#include<vector>
#include<set>

using namespace std;

pair<int, int> get_picOrFij(const string& key,const string& attempt){
    /* Funcion que verifica cuales son picas y cuales son fijas en el 
    intento del usuario, retorna las 2 variables de picas ++, fijas ++,
    recordando que fijas es que esten en la misma pocision de la llave y 
    picas en diferente posicion.*/
    int picas = 0, fijas = 0;
    for (int _=0;_<4;_++){
        for (int l=0;l<4;l++){
            if (key[_] == attempt[l]){
                picas++;
            }
        }
    }
    for (int _=0;_<4;_++){
        if (key[_] == attempt[_]){
            fijas++;
        }
    }
    return make_pair(picas,fijas);
}

string generateKey(){
    /* Funcion que genera el numero aleatorio y lo retorna, cumpliendo
    con que no se repita el numero de la llave*/
    srand(time(NULL));
    string(key);

    for(int _=0;_<4;_++){
        int ramdon = rand()%10;
        bool duplicate = false;
        for (int j=0;j<_;j++){
            if (key[j] == static_cast<char>(ramdon + '0')) {
                duplicate = true;
                break;
            }
        }
        if (!duplicate){
            key += static_cast<char>(ramdon + '0');
        } else{
            _--;
        }
    }
    return key;
}

void showMSJ(int count){
    /* Funcion que solo muestra un mensaje segun los intentos del usuario*/
    if (count<2){
        cout<<"* Excelente,eres un maestro estas fuera del alcance de los demas"<<endl;
    } else if (count<4){
        cout<<"* Muy bueno, puedes ser un gran competidor"<<endl;
    } else if (count<8){
        cout<<"* Bien, estas progresando debes buscar tus limites"<<endl;
    } else if (count<10){
        cout<<"* Regular, Aun es largo el camino por recorrer"<<endl;
    } else {
        cout<<"* Mal, este juego no es para ti"<<endl;
    }
}

int main (){
    /* Inicio del juego */
    string attempt, key;
    int count = 0, picas = 0, fijas = 0;
    key = generateKey();
    cout<<"\n\t♠ Picas & Fijas  ♠\n"<<endl;
    //cout<<key<<endl; // Descomenta si quieres ver la llave
    while (count < 12){
        cout<<"* Ingrese un numero de 4 cifras sin repetir decimales :> ";cin>>attempt;
        if ((attempt.length() != 4) || (!isdigit(attempt[0])) || (!isdigit(attempt[1]))|| (!isdigit(attempt[2]))|| (!isdigit(attempt[3]))){
            continue;
        }
        vector<int> attemptVec;
        for (char digit : attempt){
            attemptVec.push_back(digit - '0');
        }
        if (set<int>(attemptVec.begin(), attemptVec.end()).size() < 4){
            continue;
        }
        count++;

        pair<int, int> result = get_picOrFij(key, attempt);
        picas = result.first;
        fijas = result.second;

        cout<<"\n- Intento: ["<<count<<"]\n- Picas: ["<<picas<<"]\n- Fijas: ["<<fijas<<"]\n"<<endl;
        if (fijas == 4){
            showMSJ(count);break;
        }
        if (count == 12){
            showMSJ(count);
            cout<<"\nLa clave era: "<<key<<endl;
        }
    }
    return 0;
}