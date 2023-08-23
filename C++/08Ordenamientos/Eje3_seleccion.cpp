#include<iostream>

int main(){
    int numbers[] = {6,3,1,4,2,5}, aux, min;

    for (int i=0;i<6;i++){
        min = i;
        for (int j=i+1;j<6;j++){
            if (numbers[j] < numbers[min]){
                min = j;
            }
        }
        aux = numbers[i];
        numbers[i] = numbers[min];
        numbers[min] = aux;
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