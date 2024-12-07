/* 
 *  --- Day 9: All in a Single Night ---
 *  Every year, Santa manages to deliver all of his presents in a single night.
 *  
 *  This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?
 *  
 *  For example, given the following distances:
 *  
 *  London to Dublin = 464
 *  London to Belfast = 518
 *  Dublin to Belfast = 141
 *  The possible routes are therefore:
 *  
 *  Dublin -> London -> Belfast = 982
 *  London -> Dublin -> Belfast = 605
 *  London -> Belfast -> Dublin = 659
 *  Dublin -> Belfast -> London = 659
 *  Belfast -> Dublin -> London = 605
 *  Belfast -> London -> Dublin = 982
 *  The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.
 *  
 *  What is the distance of the shortest route?
 *
 */

#include "../Utils/utils.h"
#include <stdint.h>

#define INPUT_DIR "../Inputs/2015_09.txt"

extern "C" {
    FILE* openFile(char* INPUT_FILE_PATH);
    char* nextLine(FILE* file);
    void  closeFile(FILE* file);
    char** splitString(char* string, char* delimeter, int* size);
}


int main(){
    char* line = NULL;
    FILE* file = openFile((char*)INPUT_DIR);
    
    while( (line = nextLine(file)) ){
        
        int arraySize = 0;
        char** inputArr = splitString(line, (char*)" ", &arraySize);

        inputArr[0] = (char*)"x";
        line++;
    }

    closeFile(file);
    return 0;
}
