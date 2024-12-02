#include "../lib.c"

int main(int argc, char *argv[]) {
    str input = read_file_to_buffer("input.txt");
    print("{s} {d}\n", "test", input);
}