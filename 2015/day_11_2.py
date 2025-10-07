'''
--- Day 11: Corporate Policy ---
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
For example:

hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
Given Santa's current password (your puzzle input), what should his next password be?

Your puzzle input is vzbxkghb.
--- Part Two ---
Santa's password expired again. What's the next one?
'''

import req
import utils

def incdata(data):
    out_data = ''
    inc_next = True
    for i in range(len(data) - 1, -1, -1):
        if(inc_next and data[i] == 'z'):
            inc_next = True
            out_data = 'a' + out_data
        elif inc_next:
            out_data = chr(ord(data[i]) + 1) + out_data
            inc_next = False
        else:
            out_data = data[i] + out_data
    return out_data

def meetpasspolicy(data):
    two_pair = []
    is_three_pair_found = False

    for index,char in enumerate(data):
        if(data[index] in ['i', 'o', 'l']):
            return False

        if(index + 1 != len(data)):
            if(char == data[index + 1] and char not in two_pair):
                two_pair.append(char)

        if( not is_three_pair_found and index + 2 < len(data) and 
            chr(ord(data[index]) + 1) == data[index + 1] and 
            chr(ord(data[index]) + 2) == data[index + 2]
          ):
            is_three_pair_found = True
    return len(two_pair) == 2 and is_three_pair_found

def main():
    input_data = [incdata("vzbxxyzz")]

    for data in input_data:
        while not meetpasspolicy(data):
            data = incdata(data)
        print(data)

if __name__ == '__main__':
    main()