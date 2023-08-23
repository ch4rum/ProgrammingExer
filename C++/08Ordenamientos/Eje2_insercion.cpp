#include <iostream>

int main(){
    int numbers[] = {4,6,2,1,3,5}, aux, pos;

    for (int _=0;_<6;_++){
        pos = _;
        aux = numbers[_];
        while ( (pos > 0) && (numbers[pos-1] > aux) ){
            numbers[pos] = numbers[pos-1];
            pos--;
        }
        numbers[pos] = aux;
    }
    std::printf("\nOrden ascendente: ");
    for (int _=0;_<6;_++){
        std::printf("%d ",numbers[_]);
    }
    std::printf("\nOrden desendente: ");
    for (int _=5;_>=0;_--){
        std::printf("%d ",numbers[_]);
    }
    std::cout<<std::endl;
    return 0;
}