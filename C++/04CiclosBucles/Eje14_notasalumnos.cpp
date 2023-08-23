/* 14. En una clase de 5 alumnos se han realizado tres examenes y se requiere 
determinar el numero de

a) Alumnos que aprobaron todos los examenes
b) Alumnos que aprobaron al menos un examen
c) Alumnos que aprobaron el ultimo examen
Realize un programa que calcue la entrada de los y el calculo de las estadisticas */

#include<iostream>

using namespace std;

int main(){
    float noteOne, noteTwo, noteThree; 
    int tExams=0, oneExams=0, uExams=0;

    cout<<"\tExamenes Alumnos\n";
    
    for (int _=1; _<=5; _++){
        cout<<"\nAlumno "<<_<<endl;
        do {
            cout<<"Digite la nota 1: "; cin>>noteOne;
        }while((noteOne<0) || (noteOne>10));
        
        do {
            cout<<"Digite la nota 2: "; cin>>noteTwo;
        }while((noteTwo<0) || (noteTwo>10));
        
        do {
            cout<<"Digite la nota 3: "; cin>>noteThree;
        }while((noteThree<0) || (noteThree>10));

        if ((noteOne>=6)&&(noteTwo>=6)&&(noteThree>=6)){tExams ++;}
        else if ((noteOne>=6)||(noteTwo>=6)||(noteThree>=6)){oneExams ++;}
        if ((noteOne<6)&&(noteTwo<6)&&(noteThree>=6)){uExams ++;}
    }
    cout<<"\na)Los alumnos que aprobaron todos los examenes fueron :"<<tExams<<endl;
    cout<<"b)Los alumnos que aprobaron al menos un examenes fueron :"<<oneExams<<endl;
    cout<<"c)Los alumnos que aprobaron el ultimo examenes fueron :"<<uExams<<endl;
    return 0;
}