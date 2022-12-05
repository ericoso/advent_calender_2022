#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string.h>

using namespace std;

int main(){

    ifstream in_file;
    in_file.open("input.txt");
    
    if (!in_file) {
        std::cerr << "Problem opening file" << std::endl;
        return 1;
    }
    
    string line {};
    int count {0};
    
    while (getline(in_file, line)) {
        
        int dash    = line.find('-');
        int comma   = line.find(',');
        string second_line = line.substr(comma+1);
        
        int s_pos_1 = stoi(line.substr(0, dash));
        int f_pos_1 = stoi(line.substr(dash + 1, comma));
        
        dash    = second_line.find('-');
        
        int s_pos_2 = stoi(second_line.substr(0, dash));
        int f_pos_2 = stoi(second_line.substr(dash+1));
        
        if ((s_pos_2 >= s_pos_1 && s_pos_2 <= f_pos_1) || (f_pos_2 >= s_pos_1 && f_pos_2 <= f_pos_1)){
            cout << line << endl;
            count++;
        } else if ((s_pos_1 >= s_pos_2 && s_pos_1 <= f_pos_2) || (f_pos_1 >= s_pos_2 && f_pos_1 <= f_pos_2)){
            cout << line << endl;
            count++;
        }
    }
    
    cout << count;
    
    return 0;
}