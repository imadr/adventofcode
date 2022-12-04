#include <iostream>
#include <vector>
#include <string>
#include <limits>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    if (argc < 2) return 1;
    string filename(argv[1]);
    ifstream file_stream(filename);
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

    vector<int> calories;
    for (vector<int> elf : inventory) {
        int sum = 0;
        for (int food : elf) {
            sum += food;
        }
        calories.push_back(sum);
    }
    sort(calories.begin(), calories.end(), [](int a, int b) {
        return a > b;
    });
    cout << calories[0] + calories[1] + calories[2];
}