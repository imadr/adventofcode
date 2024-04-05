#include <iostream>

int main(){
    std::string input = "()())";
    int floor = 0;
    int basement = 0;
    int counter = 0;
    for(auto c : input){
        counter++;
        if(c == '('){
            floor++;
        }
        else{
            floor--;
        }
        if(floor == -1){
            basement = counter;
            break;
        }
    }
    std::cout << basement << std::endl;
    return 0;
}