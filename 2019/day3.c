#include <stdio.h>
#include <stdlib.h>

int main(){
    char board[10][11];
    int start[] = {8, 1};
    for(int j = 0; j < 10; j++){
        for(int i = 0; i < 11; i++){
            board[j][i] = '.';
        }
    }
    board[start[0]][start[1]] = 'o';

    char* wire_1[] = {"R8","U5","L5","D3"};

    int len_wire_1 = sizeof(wire_1)/sizeof(char*)

    for(int i = 0; i < len_wire_1; i++){
        printf("%s\n", wire_1[i]);
    }


    for(int j = 0; j < 10; j++){
        for(int i = 0; i < 11; i++){
            printf("%c", board[j][i]);
        }
        printf("\n");
    }
}