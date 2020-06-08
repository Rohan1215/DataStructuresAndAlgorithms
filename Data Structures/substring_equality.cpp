#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
typedef unsigned long long ull;
using namespace std;

class Solver {
	string s;
	int x;
	int prime1;
	int prime2;
	int strSize;
	vector<ull> prefixes1;
  vector<ull> powers1;
	vector<ull> prefixes2;
  vector<ull> powers2;
public:	
	Solver(string s) : s(s) {	
		strSize=s.size();
		prime1=1000000007;
		prime2=1000000009;
		x=1+rand()%1000000000;
		prefixes1.resize(strSize+1);
    powers1.resize(strSize+1);
    powers1[0]=1;
    prefixes2.resize(strSize+1);
    powers2.resize(strSize+1);
    powers2[0]=1;
    for(int i=1;i<strSize+1;i++){
      powers1[i]=(powers1[i-1]*x)%prime1;
      powers2[i]=(powers2[i-1]*x)%prime2;
    }
		prefixes1[0]=0;
    prefixes2[0]=0;
		for(int i=1;i<strSize+1;i++){
			prefixes1[i]=(x*prefixes1[i-1]+s[i-1])%prime1;
      prefixes2[i]=(x*prefixes2[i-1]+s[i-1])%prime2;
		}
/*
0 0
s[0] 1 a
s[1] 2 ax + b 
s[2] 3 axx + bx + c
s[3] 4 axxx + bxx + cx + d 
s[4] 5 axxxx + bxxx + cxx + dx + e
*/
	}
	void getHash1(int beg, int length, ull* ptr){
		int end=beg+length-1;
    ull h= ((    (prefixes1[end+1]) - (((prefixes1[beg]* powers1[length] ))%prime1)   )+prime1);
    *ptr=h;
	}
  void getHash2(int beg, int length, ull* ptr){
		int end=beg+length-1;
    ull h= ((    (prefixes2[end+1]) - (((prefixes2[beg]* powers2[length] ))%prime2)   )+prime2);
    *ptr=h;
	}
	bool ask(int a, int b, int l) {
		ull aHash1,bHash1,aHash2,bHash2;
    //cout<<endl<<endl<<"A"<<endl;
		getHash1(a,l,&aHash1);
		getHash1(b,l,&bHash1);
    getHash2(a,l,&aHash2);
		getHash2(b,l,&bHash2);
    //cout<<"B"<<endl;
    //cout<<aHash<<" "<<bHash<<endl;
		if( ( (aHash1%prime1)==(bHash1%prime1) ) && ( (aHash2%prime2) == (bHash2%prime2) ) ){
      return true;
		}
    //cout<<"here?"<<endl;
		return false;
	}
};

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0);

	string s;
	int q;
  //ifstream in ("input.in");
	cin >> s >> q;
	Solver solver(s);
	for (int i = 0; i < q; i++) {
		int a, b, l;
		cin >> a >> b >> l;
    //cout<<endl<<endl<<endl;
    bool equal=solver.ask(a,b,l);
    if(equal) cout<<"Yes"<<endl;
		else cout << "No"<<endl;
	}
}
