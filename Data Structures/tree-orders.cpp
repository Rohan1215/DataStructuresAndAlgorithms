#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node{
  int key;
  int left;
  int right;
};
vector <Node> tree;



void DFSpreOrder(int n){
  if(n==-1) return;
  cout<<tree[n].key<<" ";  
  DFSpreOrder(tree[n].left);
  DFSpreOrder(tree[n].right);
}

void DFSinOrder(int n){
  if(n==-1) return;  
  DFSinOrder(tree[n].left);
  cout<<tree[n].key<<" ";
  DFSinOrder(tree[n].right);
}

void DFSpostOrder(int n){
  if(n==-1) return;  
  DFSpostOrder(tree[n].left);
  DFSpostOrder(tree[n].right);
  cout<<tree[n].key<<" ";
}
int main() {
  ios_base::sync_with_stdio(0);
  int n;
  cin>>n;
  tree.resize(n);
  for(int i=0;i<n;i++){
    cin>>tree[i].key>>tree[i].left>>tree[i].right;
  }
  DFSinOrder(0);
  cout<<endl;
  DFSpreOrder(0);
  cout<<endl;
  DFSpostOrder(0);
  cout<<endl;
  return 0;
}


