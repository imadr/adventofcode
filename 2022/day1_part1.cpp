#include <iostream>
#include <vector>
#include <string>
#include <limits>
#include <fstream>
#include <sstream>

#include <chrono>

using namespace std;

void benchmark(void(*func)(), int repeat, int number_runs) {
    double smallest = std::numeric_limits<double>::infinity();
    for (int i = 0; i < repeat; i++) {
        auto t0 = std::chrono::high_resolution_clock::now();
        for (int j = 0; j < number_runs; j++) {
            func();
        }
        auto t1 = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> delta = t1 - t0;
        if (delta.count() < smallest) {
            smallest = delta.count();
        }
    }
    std::cout << smallest << " SEC" << std::endl;
}

void func() {
    ifstream file_stream("input.txt");
    stringstream buffer;
    buffer << file_stream.rdbuf();
    string input = buffer.str();

    vector<vector<int>> inventory = {
        {},
    };
    size_t index = 0;
    int elf = 0;
    while ((index = input.find('\n')) != string::npos) {
        string token = input.substr(0, index);
        if (token == "") {
            inventory.push_back({});
            elf++;
        } else {
            inventory[elf].push_back(stoi(token));
        }
        input.erase(0, index + 1);
    }
    string token = input.substr(0, index);
    inventory[elf].push_back(stoi(token));

    int max = -numeric_limits<int>::infinity();
    for (vector<int> elf : inventory) {
        int sum = 0;
        for (int food : elf) {
            sum += food;
        }
        if (sum > max) {
            max = sum;
        }
    }
    int res = max;
}

int main(int argc, char *argv[]) {
    benchmark(func, 50, 100);
    // if (argc < 2) return 1;
    // string filename(argv[1]);
    // ifstream file_stream(filename);
    // stringstream buffer;
    // buffer << file_stream.rdbuf();
    // string input = buffer.str();

    // vector<vector<int>> inventory = {
    //     {},
    // };
    // size_t index = 0;
    // int elf = 0;
    // while ((index = input.find('\n')) != string::npos) {
    //     string token = input.substr(0, index);
    //     if (token == "") {
    //         inventory.push_back({});
    //         elf++;
    //     } else {
    //         inventory[elf].push_back(stoi(token));
    //     }
    //     input.erase(0, index + 1);
    // }

    // int max = -numeric_limits<int>::infinity();
    // for (vector<int> elf : inventory) {
    //     int sum = 0;
    //     for (int food : elf) {
    //         sum += food;
    //     }
    //     if (sum > max) {
    //         max = sum;
    //     }
    // }
    // cout << max;
}