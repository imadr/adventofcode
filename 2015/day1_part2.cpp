#include <iostream>

int main(){
    std::string input = "(()(()(";
    int floor = 0;
    for(auto c : input){
        if(c == '('){
            floor++;
        }
        else{
            floor--;
        }
    }
    std::cout << floor << std::endl;
    return 0;
}