#include <algorithm>
#include <iostream>
#include <vector>
#include <bits/stdc++.h> 

using namespace std;

struct Node {
  long key;
  int left;
  int right;
  Node() : key(0), left(-1), right(-1) {}
  Node(int key_, int left_, int right_) : key(key_), left(left_), right(right_) {}
};
Node tree [100001];
bool IsBST(int n, long mn, long mx) {
  if(n<0)return true;
  if(!(tree[n].key>mn && tree[n].key<mx)) return false;
  bool l= IsBST(tree[n].left,mn,tree[n].key);
  bool r= IsBST(tree[n].right,tree[n].key,mx);
  return l&r;
}

int main() {
  int n;
  cin>>n;
  for(int i=0;i<n;i++){
    cin>>tree[i].key>>tree[i].left>>tree[i].right;
  }
  if (IsBST(0,-2500000000,2500000000)) {
    cout << "CORRECT" << endl;
  } else {
    cout << "INCORRECT" << endl;
  }
  return 0;
}
