#ifndef _UTILS_H_
#define _UTILS_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_LINE_LENGTH 1024

char** splitString(char* string, char* delimeter, int* size);

FILE* openFile(char* INPUT_FILE_PATH);
char* nextLine(FILE* file);
void  closeFile(FILE* file);

#ifdef __cplusplus
}
#endif

#endif /* _UTILS_H_ */