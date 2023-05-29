/* 7. La calificacion final de un estudainte es la media ponderada de 3 notas:
La nota ded practicas que cuenta un 30% del total, la nota teorica que
cuenta un 60% y la nota de participacion que cuenta con el 10% restante.
Escriba un programa que lea la entrada estadar las 3 notas de un alumno
y escriba en la salida estandar su nota final*/

#include<iostream>

using namespace std;

int main(){
    float note1Practice, note2Theoretical, note3Participation, endNotes = 0;

    cout<<"Digite la nota de practica: "; cin>>note1Practice;
    cout<<"Digite la nota teorica: "; cin>>note2Theoretical;
    cout<<"Digite la nota de participacion: "; cin>>note3Participation;

    note1Practice *= 0.30;
    note2Theoretical *= 0.60;
    note3Participation *= 0.10;

    endNotes = note1Practice + note2Theoretical + note3Participation;
    // cout.precision(2);
    cout<<"\nLa nota final es: "<<endNotes<<endl;

    return 0;
}