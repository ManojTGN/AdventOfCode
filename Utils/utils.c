#include "utils.h"

FILE* openFile(char* INPUT_FILE_PATH) {
    FILE *file = fopen(INPUT_FILE_PATH, "r");

    if (file == NULL) {
        perror("Error opening file");
        return NULL;
    }

    return file;
}

char* nextLine(FILE* file){
    char* line = calloc(MAX_LINE_LENGTH,sizeof(char));

    char* result = fgets(line, sizeof(line), file);
    if(!result) return NULL;

    return line;
}

void closeFile(FILE* file){
    fclose(file);
}

