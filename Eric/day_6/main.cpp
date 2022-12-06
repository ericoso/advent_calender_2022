#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

bool is_unique (string in);

int main(){
    
    ifstream in_file;
    in_file.open("input.txt");
    
    if (!in_file) {
        std::cerr << "Problem opening file" << std::endl;
        return 1;
    }
    
    string line {};
    getline(in_file, line);
    int i = 0;
    
    while (true){
        
        cout << i + 1 << ") ";
        string temp = line.substr(0 + i, 14);
        if (is_unique(temp)){
            cout << i + 14 << endl;
            break;
        }
        i++;
    }    

    return 0;   
}

bool is_unique (string in){
    for (int i = 0; i < (in.size() - 1); i++){
        for (int j = i + 1; j < in.size(); j++){
            if (in[i] == in[j]){
                cout << in << " : " << in[i] << " equals " << in[j] << " on positions " << i << "," << j << endl;
                return false;
            }
        }
    }
    cout << in << " is the first!" << endl;
    return true;
}