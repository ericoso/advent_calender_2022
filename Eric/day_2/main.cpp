#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int main(){

//Starting file & checking file
    ifstream in_file;
    in_file.open("guild.txt");
    
    if (!in_file) {
        std::cerr << "Problem opening file" << std::endl;
        return 1;
    }
    
    string line{};
    vector<char> inputs_c{};
    vector<char> outcomes_c{};
    
    
    while (getline(in_file, line)) {
        inputs_c.push_back(line[0]);
        outcomes_c.push_back(line[2]);
    }
    
    vector<int> inputs_i{};
    vector<int> responses_i{};
    vector<int> outcomes_i{};
    
    for (char input:inputs_c){
        switch (input){
            case 'A':
                inputs_i.push_back(1);
                break;
            case 'B':
                inputs_i.push_back(2);
                break;
            case 'C':
                inputs_i.push_back(3);
                break;
        }        
    }
    
    for (char outcome:outcomes_c){
        switch (outcome){
            case 'X':
                outcomes_i.push_back(-1);
                break;
            case 'Y':
                outcomes_i.push_back(0);
                break;
            case 'Z':
                outcomes_i.push_back(+1);
                break;
        }        
    }
    
    for (unsigned int i = 0; i < inputs_i.size(); i++){
        int response = inputs_i.at(i) + outcomes_i.at(i);
        
        if (response == 0){
            response = 3;
        }

        if (response == 4){
            response = 1;
        }
        
        responses_i.push_back(response);
    }
    
    int t_points{};
    
    for (unsigned int i = 0; i < inputs_i.size(); i++){
        int outcome = -inputs_i.at(i) + responses_i.at(i);
        switch (outcome){
            case -2:
                t_points += 6;
                break;
            case -1:
                break;
            case 0:
                t_points += 3;
                break;
            case 1:
                t_points += 6;
                break;
            case 2:
                break;
        }
        t_points += (responses_i.at(i));
    }
    
    cout << t_points;

 return 0;    
}