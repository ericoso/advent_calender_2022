#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int main(){
    
    //Starting file & checking file
    ifstream in_file;
    in_file.open("calories.txt");
    
    if (!in_file) {
        std::cerr << "Problem opening file" << std::endl;
        return 1;
    }
    
    //initialising variables for extracting and saving data
    vector<int> elf_calories;
    string line{};
    int t_calories = 0; //total_
    
    //extracting line by line adding and setting to vector per elf
    while (getline(in_file, line)) {
        if (line != ""){
            t_calories += stoi(line);
        } else {
            elf_calories.push_back(t_calories);
            t_calories = 0;
        }
    }
    
    //sorting n_calories per elf
    sort(elf_calories.begin(), elf_calories.end(), greater <>());
    //calculating totoal calories of the top 3
    t_calories = elf_calories.at(0) + elf_calories.at(1) + elf_calories.at(2);
    cout << t_calories;
    
    return 0;
}
