/* 
* Discrete Mathematics Example Problems
* Practicing the concept of set combinations and permuations
* Class Notes 11/13/2023
* Factorial - of a positive int is the sum of multiplication
* of all the integers smaller than that positive integer. 
*/
#include <vector>
#include <iostream>
#include <algorithm>

// Make a function that returns the number factorial: 
int calculate_factorial(int n){
    if (n == 0 || n == 1){
        return 1; 
    }
    std::vector<int> upto; 
    int product = n; 
    for (int i = 1; i < n; i++){
        upto.push_back(i); 
    }
    /*std::cout << "Multiplying all numbers up to: ";  
    for (int i = 0; i < upto.size(); i++){
        std::cout << upto[i] << ' ';     
    }*/
    reverse(upto.begin(), upto.end()); 
    for (int i = 0; i < upto.size(); i++){
        product *= upto[i]; 
    }
    return product; 
}

int main(){
    std::cout << "What is the number you want the factorial for (integer; max 19): "; 
    int n;  
    std::cin >> n; 
    std::cout << "\nThis is the factorial of " << n << " is " << calculate_factorial(n); //Can work on combinations, factorial works.  
    return 0; 
}
