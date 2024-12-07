#include "utils.h"

FILE* openFile(char* INPUT_FILE_PATH) {
    FILE *file = fopen(INPUT_FILE_PATH, "r");

    if (file == NULL) {
        perror("Error Opening The Input File.");
        return NULL;
    }

    return file;
}

char* nextLine(FILE* file){
    char* line = calloc(MAX_LINE_LENGTH,sizeof(char));

    char* result = fgets(line, MAX_LINE_LENGTH, file);
    if(!result) return NULL;
    result[strcspn(result, "\n")] = '\0'; 

    return line;
}

void closeFile(FILE* file){
    fclose(file);
}

char** splitString(char* string, char* delimeter, int* size){
    
}

