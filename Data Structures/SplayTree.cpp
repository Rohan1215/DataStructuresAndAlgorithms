#include <cstdio>
#include <vector>
#include <bits/stdc++.h> 

using namespace std;
// Splay tree implementation

// Node of a splay tree
struct Node {
  int key;
  // Sum of all the keys in the subtree - remember to update
  // it after each operation that changes the tree.
  long long sum;
  Node* left;
  Node* right;
  Node* parent;

  Node(int key, long long sum, Node* left, Node* right, Node* parent) 
  : key(key), sum(sum), left(left), right(right), parent(parent) {}
};

void update(Node* v) {
  if (v == NULL) return;
  //v's sum is the sum of left and right subtree
  v->sum = v->key + (v->left != NULL ? v->left->sum : 0ll) + (v->right != NULL ? v->right->sum : 0ll);
  //set child's parent to v
  if (v->left != NULL) {
    v->left->parent = v;
  }
  if (v->right != NULL) {
    v->right->parent = v;
  }
}

void small_rotation(Node* v) {
  Node* parent = v->parent;
  if (parent == NULL) {
    //root
    return;
  }
  Node* grandparent = v->parent->parent;
  if (parent->left == v) {
    //left child, less than parent v<m<p
    /*
        (P)          (v) 
       /               \  
      (v)      --->     (P)   
        \               /
         (m)           (m)
    */
    Node* m = v->right;
    v->right = parent;
    parent->left = m;
  } 
  else {
    //right child, greater than parent
    Node* m = v->left;
    v->left = parent;
    parent->right = m;
  }
  update(parent);
  update(v);
  // fix P's parent
  v->parent = grandparent;
  if (grandparent != NULL) {
    if (grandparent->left == parent) {
      grandparent->left = v;
    } else {
      grandparent->right = v;
    }
  }
}

void big_rotation(Node* v) {
  if (v->parent->left == v && v->parent->parent->left == v->parent) {
    // Zig-zig
    small_rotation(v->parent);
    small_rotation(v);
  } 
  else if (v->parent->right == v && v->parent->parent->right == v->parent) {
    // Zig-zig
    small_rotation(v->parent);
    small_rotation(v);
  } 
  else {
    // Zig-zag
    small_rotation(v);
    small_rotation(v);
  }  
}

// Makes splay of the given Node and makes
// it the new root.
void splay(Node*& root, Node* v) {
  if (v == NULL) return;
  while (v->parent != NULL) {
    if (v->parent->parent == NULL) {
      small_rotation(v);
      break;
    }
    big_rotation(v);
  }
  root = v;
}

// Searches for the given key in the tree with the given root
// and calls splay for the deepest visited node after that.
// If found, returns a pointer to the node with the given key.
// Otherwise, returns a pointer to the node with the smallest
// bigger key (next value in the order).
// If the key is bigger than all keys in the tree, 
// returns NULL.
Node* find(Node*& root, int key) {
  Node* v = root;
  Node* last = root;
  Node* next = NULL;
  while (v != NULL) {
    if (v->key >= key && (next == NULL || v->key < next->key)) {
      next = v;
    }
    last = v;
    if (v->key == key) {
      break;      
    }
    if (v->key < key) {
      v = v->right;
    } 
    else {
      v = v->left;
    }
  }
  splay(root, last);
  return next;
}

void split(Node* root, int key, Node*& left, Node*& right) {
  
  right = find(root, key);
  if (right == NULL) {
    left = root;
    return;
  }
  splay(root, right);
  left = right->left;
  right->left = NULL;
  if (left != NULL) {
    left->parent = NULL;
  }
  update(left);
  update(right);
}

Node* merge(Node* left, Node* right) {
  if (left == NULL) return right;
  if (right == NULL) return left;
  Node* min_right = right;
  while (min_right->left != NULL) {
    min_right = min_right->left;
  }
  splay(right, min_right);
  right->left = left;
  update(right);
  return right;
}

// Code that uses splay tree to solve the problem

Node* root = NULL;

void insert(int x) {
  Node* left = NULL;
  Node* right = NULL;
  Node* new_Node = NULL;  
  split(root, x, left, right);
  if (right == NULL || right->key != x) {
    new_Node = new Node(x, x, NULL, NULL, NULL);
  }
  root = merge(merge(left, new_Node), right);
}

void erase(int x) {                
  Node* ele=find(root,x);
  if(ele==NULL)return;
  if(ele->key!=x) return;
  splay(root,ele);
  root = merge(ele->left,ele->right);
  if(root!=NULL) root->parent=NULL;

}  
bool search(int x) {  
  if(root==NULL)return false;
  Node* ele=find(root,x);
  if(ele==NULL) return false;
  return (ele->key==x);
}

long long sum(int from, int to) {
  Node* left = NULL;
  Node* middle = NULL;
  Node* right = NULL;
  split(root, from, left, middle);
  split(middle, to + 1, middle, right);
  long long ans= (middle==NULL)?0:middle->sum;
  root=merge(left,merge(middle,right));
  
  return ans;  
}

const int MODULO = 1000000001;

int main(){
  int n;
  scanf("%d", &n);
  int last_sum_result = 0;
  for (int i = 0; i < n; i++) {
    char buffer[10];
    scanf("%s", buffer);
    char type = buffer[0];
    switch (type) {
      case '+' : {
        int x;
        scanf("%d", &x);
        insert((x + last_sum_result) % MODULO);
      } break;
      case '-' : {
        int x;
        scanf("%d", &x);
        erase((x + last_sum_result) % MODULO);
      } break;            
      case '?' : {
        int x;
        scanf("%d", &x);
        printf(search((x + last_sum_result) % MODULO) ? "Found\n" : "Not found\n");
      } break;
      case 's' : {
        int l, r;
        scanf("%d %d", &l, &r);
        long long res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO);
        printf("%lld\n", res);
        last_sum_result = int(res % MODULO);
      }
    }
  }
  return 0;
}
