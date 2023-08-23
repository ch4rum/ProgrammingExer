#include <iostream>

int main() {
    int aux, numbers[] = {4,6,3,1,5,2};

    for (int i=0;i<6;i++){
        for (int j=0;j<5;j++){
            if (numbers[j] > numbers[j+1]){
                aux = numbers[j];
                numbers[j] = numbers[j+1];
                numbers[j+1] = aux;
            }
        }
    }
    std::printf("Orden ascendente: ");
    for (int _=0;_<6;_++){
        std::printf("%d ",numbers[_]);
    }
    std::printf("\nOrden Desendente: ");
    for (int _=5;_>=0;_--){
        std::printf("%d ",numbers[_]);
    }
    std::cout<<std::endl;
    return 0;
}