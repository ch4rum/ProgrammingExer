/* 5. Hacer un programa que determine si una palabra es palindromo*/

#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;

int main(){
    char palindr[100], copypalindr[100];
    cout<<"Digite una palabra: "; 
    cin>>palindr;
    strcpy(copypalindr,palindr);
    reverse(copypalindr, copypalindr + strlen(copypalindr));
    
    if(strcmp(palindr,copypalindr) == 0){
        cout<<"Es un palindromo \n";
    } else {
        cout<<"No es un palindromo \n";
    }

    return 0;
}