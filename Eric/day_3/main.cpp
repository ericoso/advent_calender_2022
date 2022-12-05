#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int main(){

    ifstream in_file;
    in_file.open("input.txt");
    
    if (!in_file) {
        std::cerr << "Problem opening file" << std::endl;
        return 1;
    }
    
    string line{};
    vector<string> elves{};
    vector<char> answer{};

    
    while (getline(in_file, line)) {
        elves.push_back(line);
    }
    
    for (int i = 0; i < elves.size(); i = i + 3){
        vector<char> doubles{};
        for (auto letter: elves.at(i)){
            if(elves.at(i+1).find(letter) != 18446744073709551615){
                doubles.push_back(letter);
            }
        } 
        for (auto letter: doubles){
            if(elves.at(i+2).find(letter) != 18446744073709551615){
                answer.push_back(letter);
                break;
            }
        }
    }
    
    int t_val{};
    
    for(auto letter: answer){
        int x = letter;
        cout << letter << " : " << x << " : ";
        
        if(isupper(letter)){
            cout << (x - 65 + 27) << endl;
            t_val += (x - 65 + 27);
        } else {
            cout << (x - 97 + 1) << endl;
            t_val += (x - 97 + 1);
        }
    }
    
    cout << endl << endl << t_val;
    
    
    return 0;
    
}