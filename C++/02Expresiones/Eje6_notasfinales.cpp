/* 6. Escriba un programa que lea la nota final de 4 alumnos y 
calcule la nota final media de los 4 alumnos*/

#include<iostream>

using namespace std;

int main(){
    float note1,note2,note3,note4, endNote = 0;

    cout<<"Digite la 1era nota: "; cin>>note1;
    cout<<"Digite la 2da nota: "; cin>>note2;
    cout<<"Digite la 3ra nota: "; cin>>note3;
    cout<<"Digite la 4ta nota: "; cin>>note4;

    endNote = (note1 + note2 + note3 + note4) / 4;

    cout.precision(2);
    cout<<"\nLa nota final media es: "<<endNote<<endl;

    return 0;
}