#include <iostream>
#include <ctime>
#include <fstream>
#include <cstring>

using namespace std;

void showHelp(){
    printf("\nUso: ./Ordenamientos [-h] [-b </archivo?>] [-s </archivo?>] [-i </archivo?>] [-m </archivo?>] [-q </archivo?>] [-v]\n\n");
    printf("Programa para Analizar algoritmos de ordenamiento\n\n");
    printf("Options:\n");
    printf("  -h, --help            Muestra esta ayuda y sale.\n\n");
    printf("  -b </archivo?>, --bubble </archivo?>\n");
    printf("                        Pasar archivo con datos para el algoritmo de Burbuja.\n\n");
    printf("  -s </archivo?>, --selection </archivo?>\n");
    printf("                        Pasar archivo con datos para el algoritmo de Seleccion.\n\n");
    printf("  -i </archivo?>, --insertion </archivo?>\n");
    printf("                        Pasar archivo con datos para el algoritmo de Insercion.\n\n");
    printf("  -m </archivo?>, --mergesort </archivo?>\n");
    printf("                        Pasar archivo con datos para el algoritmo de Mergesort.\n\n");
    printf("  -q </archivo?>, --quicksort </archivo?>\n");
    printf("                        Pasar archivo con datos para el algoritmo de Quicksort.\n\n");
    printf("  -v, --version         Muestra la version del programa y sale.\n\n");
}

int* openArchive(const string& filename,int& count){
    fstream archive(filename.c_str());
    if (archive.is_open()){
        int num, tempData[80000], n=0;
        while (archive >> num){
            tempData[n] = num;
            n++;
        }
        archive.close();
        count = n;
        int* data = new int[count];
        for (int _=0;_<count;_++){
            data[_] = tempData[_];
        }
        return data;
    } else {
        return NULL;
    }
}

void bubbleSort(int* data,int count){
    int aux;

    for (int i=0;i<count;i++){
        for (int j=0;j<count-1;j++){
            if (data[j] > data[j+1]){
                aux = data[j];
                data[j] = data[j+1];
                data[j+1] = aux;
            }
        }
    }
}

void selectionSort(int* data, int count){
    int aux, min;

    for (int i=0;i<count;i++){
        min = i;
        for (int j=i+1;j<count;j++){
            if (data[j] < data[min]){
                min = j;
            }
        }
        aux = data[i];
        data[i] = data[min];
        data[min] = aux;
    }
}

void insertionSort(int* data, int count){
    int aux, pos;

    for (int _=0;_<count;_++){
        pos = _;
        aux = data[_];
        while ( (pos > 0) && (data[pos-1] > aux) ){
            data[pos] = data[pos-1];
            pos--;
        }
        data[pos] = aux;
    }
}

int main(int argc, char* argv[]){

    if (argc == 2){
        string argument = argv[1];
        if ((argument == "-h") || (argument == "--help")){
            showHelp();
            return 0;
        } else if ((argument == "-v") || (argument == "--version")){
            printf("Ordenamientos v1.0\n");
            return 0;
        } else {
            printf("\nError: Utiliza --help o -h para la ayuda.\n\n");
            return 1;
        }
    } else if (argc <3){
        printf("\nError: Utiliza --help o -h para la ayuda.\n\n");
        return 1;
    } else if (argc > 2){
        char* algorithm = argv[1];
        char* filename = argv[2];
        int count;
        int* data = openArchive(filename,count);
        if (data == NULL){
            cerr<<"\nNo se pueden Ordenar datos vacios o el archivo no se pudo abrir.\n"<<endl;
            return 1;
        }
        if ((strcmp(algorithm,"-b")==0) || (strcmp(algorithm,"--bubble")==0)){
            bubbleSort(data,count);
            for (int _=0;_<count;_++){
                printf("%d - ",data[_]);
            }
        } else if ((strcmp(algorithm,"-s")==0) || (strcmp(algorithm,"--selection")==0)){
            selectionSort(data,count);
            for (int _=0;_<count;_++){
                printf("%d - ",data[_]);
            }
        } else if ((strcmp(algorithm,"-i")==0) || (strcmp(algorithm,"--insertion")==0)){
            insertionSort(data,count);
            for (int _=0;_<count;_++){
                printf("%d - ",data[_]);
            }
        }
    }
    return 0;
}