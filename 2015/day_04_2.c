/*
 *   --- Day 4: The Ideal Stocking Stuffer ---
 *   Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.
 *   To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
 *
 *   For example:
 *   If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
 *   If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
 *
 *   --- Part Two ---
 *   Now find one that starts with six zeroes.
 */

#include <stdint.h>
#include <stdio.h>

//https://github.com/Zunawe/md5-c
#include "../include/md5.h"
#define DECIMAL 10

int main(void*){
    
    uint8_t result[16];
    
    char input[20] = "bgvyzdsv";
    char tmpInp[20]= "bgvyzdsv";
    char buff[10];

    int i = 0;
    for(i = 0; i < INT_MAX; i++){
        itoa(i,buff,DECIMAL);
        strcat(tmpInp, buff);

        md5String(tmpInp, result);
        if(0x00==result[0] && 0x00==result[1] && 0x00 == result[2]) break;

        strcpy(tmpInp,input);
    }

    printf("%d [%d]", i, INT_MAX);

    return 0;
}