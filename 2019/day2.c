#include <stdio.h>
#include <stdlib.h>

int run_program(int* program, int len){
    int opcode;
    for(int i = 0; i < len; i+=4){
        opcode = program[i];
        if(opcode == 99){
            break;
        }
        else if(opcode == 1 || opcode == 2){
            if(i+3 >= len || i+2 >= len || i+1 >= len){
                break;
            }
            if(program[i+3] >= len || program[i+2] >= len || program[i+1] >= len){
                break;
            }

            if(opcode == 1){
                program[program[i+3]] = program[program[i+1]]+program[program[i+2]];
            }
            else if(opcode == 2){
                program[program[i+3]] = program[program[i+1]]*program[program[i+2]];
            }
        }
        else{
            break;
        }
    }
    return program[0];
}

int main(){
    int original_program[] = {1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,2,13,23,27,2,27,13,31,2,31,10,35,1,6,35,39,1,5,39,43,1,10,43,47,1,5,47,51,1,13,51,55,2,55,9,59,1,6,59,63,1,13,63,67,1,6,67,71,1,71,10,75,2,13,75,79,1,5,79,83,2,83,6,87,1,6,87,91,1,91,13,95,1,95,13,99,2,99,13,103,1,103,5,107,2,107,10,111,1,5,111,115,1,2,115,119,1,119,6,0,99,2,0,14,0};
    int program_len = sizeof(original_program)/sizeof(int);
    int program_size = sizeof(original_program);

    int noun, verb;
    for(int i = 0; i <= 99; i++){
        for(int j = 0; j <= 99; j++){
            int* program = malloc(program_size);
            for(int k = 0; k < program_len; k++){
                program[k] = original_program[k];
            }
            program[1] = i;
            program[2] = j;

            int output = run_program(program, program_len);
            if(output == 19690720){
                noun = i;
                verb = j;
                break;
            }
        }
    }
    printf("%d\n", noun*100+verb);
}