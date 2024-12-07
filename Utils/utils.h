#ifndef _UTILS_H_
#define _UTILS_H_

#include <stdio.h>
#include <stdlib.h>

#define MAX_LINE_LENGTH 1024

FILE* openFile(char* INPUT_FILE_PATH);
char* nextLine(FILE* file);
void  closeFile(FILE* file);

#endif /* _UTILS_H_ */