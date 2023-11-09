/* Discrete Mathematics Example Problems
* Practicing the concept of set combinations and permuations
* Class Notes 11/8/2023
*/
#include <cmath>
#include <iostream>
#include <vector>
#include <string>

int main(){
    std::cout << "how many 3 digit numbers are divisible by 5, up to 499?\n"; 
    std::vector <int> a_var;  
    for (int i = 0; i < 499; i++){
        a_var.push_back(i); 
    }
    int numbers_divisible = 0; 
    for (int i = 100; i < 499; i++){ 
        if (int x = i % 5){
            //std::cout << "the number " << i << " has a remainder of " << x << "\n";  
            continue; 
        } 
        else{
            numbers_divisible += 1; 
        }
    }
    std::cout << "there are " << numbers_divisible << " 3 digit numbers divisible by 5. \n";  
    
    std::cout << "\nconsider a 4 digit pin taken from the roman alphabet and ten digits.\n"
              << "how many pins are possible?\n"; 
    std::vector<int> digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; 
    std::vector<char> roman_alphabet;
    char alphabet = 65;   
    for (int i = 0; i < 23; i++){
        if (alphabet == 74){
            alphabet += 1; 
        }
        else if (alphabet == 85){
            alphabet += 1; 
        }
        else if (alphabet == 87){
            alphabet += 1; 
        }
        roman_alphabet.push_back(alphabet);
        alphabet += 1;  
        
    } 
    int r = digits.size(); 
    int s = roman_alphabet.size();
    long factorial_one = 1.0;
    long factorial_two = 1.0;    
    for (int i = 0; i <= r; i++){
        factorial_one *= i; 
    }
    for (int i = 0; i <= s; i++){
        factorial_two *= i; 
    }
    int total_combinations = factorial_one * factorial_two; // Leave off here: This formula is not right! 
    std::cout << "The total combinations for a 4 digit pin is " << total_combinations; 

    
    // what about with no repeated values? 
    // how many pins contain at least one repeated value? 

    // consider all integers from 1 to 1000. how many numbers are multiples by of 3 or 5? 
    // let a be multiples of 3. {3, 6, 9,....,999}
    // 3 be mulltiples of 5. {5,10,15,.....,1000} 
    return 0; 
}