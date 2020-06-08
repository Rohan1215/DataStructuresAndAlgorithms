#include <iostream>
#include <string>
#include <vector>
#include <math.h>
//#include <fstream>

using namespace std;
typedef unsigned long long ull;
int strSize=1;
struct Data {
    string pattern, text;
};

Data read_input() {
    Data data;
  //  ifstream in("input.in");
    cin >> data.pattern >> data.text;
    strSize=data.pattern.size();
    return data;
}

void print_occurrences(const vector<int>& output) {
    for (size_t i = 0; i < output.size(); ++i)
        cout << output[i] << " ";
    cout << "\n";
}
bool areEqual(string a, string b){
    for(int i=0;i<strSize;i++){
        if(a[i]!=b[i]) return false;
    }
    return true;
}
void PolyHash(string s, int x, int p, ull* h){
  for (int i = s.size() - 1; i >= 0; --i)
        *h = (*h * x + s[i]) % p;

}
vector<int> get_occurrences(const Data& input) {
    const string& s = input.pattern, t = input.text;
    vector<int> workingIndices;
    if(t.size()==s.size()){
      if(areEqual(s, t)) workingIndices.push_back(0);
      return workingIndices; 
    }
    int multiplier = rand() % 1000000007;
    int prime = 1000000007;
    ull hash = 0;
    ull actualHash=0;
    ull hashes[t.size()-s.size()+1];
    for (int i = s.size() - 1; i >= 0; --i)
        actualHash = (actualHash * multiplier + s[i]) % prime;

    for(int i=t.size()-1;i>=t.size()-strSize;--i){
        hash=(hash*multiplier+t[i])%prime;
    }
    //cout<<"****"<<endl<<actualHash<<endl<<hash<<endl<<"*****"<<endl<<endl<<"output: "<<endl;

    //cout<<t.size()-strSize<<" "<<hash<<endl;
    hashes[t.size()-strSize]=hash;
    ull y=1;
    for(int i=1;i<strSize+1;i++){
      y=(y*multiplier)%prime;
    }
    for(int i=t.size()-strSize-1;i>=0;i--){
        hashes[i]=(multiplier*hashes[i+1]+t[i]-y*t[i+strSize])%prime;
    }

    
    for(int i=0;i<t.size()-s.size()+1;i++){
     //   cout<<i<<" "<<hashes[i]<<endl;
     // cout<<i<<" "<<hashes[i]<<endl;
        if(actualHash==hashes[i]) workingIndices.push_back(i);
    } 

    
    /*cout<<"actual: "<<endl;
    for(int i=0;i<t.size()-s.size()+1;i++){
      ull hach=0;
      PolyHash(t.substr(i,i+strSize), multiplier, prime, &hach);
      cout<<i<<" "<<hach<<endl;
    } 
    */
    return workingIndices;
}


int main() {
    ios_base::sync_with_stdio(false);
    print_occurrences(get_occurrences(read_input()));
    return 0;
}
