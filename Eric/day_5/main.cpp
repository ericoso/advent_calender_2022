#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string.h>

using namespace std;





int main(){
    
    //to lazy to purge the cube's and extract the data
    vector<vector<char>> input_arr = {
    { 'G','J','W','R','F','T','Z'},
    { 'M','W','G'},
    { 'G','H','N','J'},
    { 'W','N','C','R','J'},
    { 'M','V','Q','G','B','S','F','W'},
    { 'C','W','V','D','T','R','S'},
    { 'V','G','Z','D','C','N','B','H'},
    { 'C','G','M','N','J','S'},
    { 'L','D','J','C','W','N','P','G'}
};
    
    //did it in reverse, to lazy to re-write array in reverse
    for (size_t i = 0; i < input_arr.size(); i++){
        reverse(input_arr[i].begin(), input_arr[i].end());
    }

    ifstream in_file;
    in_file.open("input.txt");
    
    if (!in_file) {
        std::cerr << "Problem opening file" << std::endl;
        return 1;
    }
    
    string line {};
    int _n = 0;
    
    while (getline(in_file, line)) {
        line = line.substr(5);
        int space = line.find(' ');
        int n_opperations = stoi(line.substr(0, space));
        line = line.substr(space + 6);
        int from    =   stoi(line.substr(0,1));
        int to      =   stoi(line.substr(5));
        
        vector<char> temp {};
        for (int i = 0; i < n_opperations; i++){
            temp.insert(temp.begin(), input_arr[from-1].back());
            input_arr[from-1].pop_back();
        }
        
        input_arr[to-1].insert(end(input_arr[to-1]), begin(temp), end(temp));
    }

for (int i = 0; i < input_arr.size(); i++){
    cout << input_arr[i].back();
} 

    return 0;
}