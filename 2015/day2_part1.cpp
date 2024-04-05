#include <iostream>
#include <cmath>
#include <string>

int main(){
    std::string input = R"(2x3x4
1x1x10)";

    input += "\n";
    std::string buffer = "";
    int total_total = 0;
    int counter = -1;
    int l, w, h;
    for(int i = 0; i < input.size(); i++){
        if(input[i] == 'x' || input[i] == '\n'){
            counter++;
            if(counter == 0){
                l = std::stoi(buffer);
                buffer = "";
            }
            else if(counter == 1){
                w = std::stoi(buffer);
                buffer = "";
            }
            else if(counter == 2){
                h = std::stoi(buffer);
                int side1 = l*w;
                int side2 = w*h;
                int side3 = h*l;
                int total = 2*side1+2*side2+2*side3+std::min(side1, std::min(side2, side3));
                total_total += total;
                counter = -1;
                buffer = "";
            }
        }
        else{
            buffer += input[i];
        }
    }
    std::cout << total_total << std::endl;
    return 0;
}