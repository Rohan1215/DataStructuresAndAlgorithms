#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::cin;
using std::cout;
using std::pair;
using std::make_pair;
int N;
class HeapBuilder {
 private:
  vector<int> data;
  vector< pair<int, int> > swaps;

  void WriteResponse() const {
    cout << swaps.size() << "\n";
    for (int i = 0; i < swaps.size(); ++i) {
      cout << swaps[i].first << " " << swaps[i].second << "\n";
    }
  /*
    cout<<std::endl<<std::endl<<std::endl;
    for(int i:data){
      cout<<i<<" ";
    }
  */
  }

  void ReadData() {
    cin >> N;
    data.resize(N);
    for(int i = 0; i < N; ++i)
      cin >> data[i];
  }

  void swap(int index1, int index2){
    swaps.push_back(make_pair(index1,index2));
    int temp=data[index1];
    data[index1]=data[index2];
    data[index2]=temp;
  }
  void siftDown(int index){
    int l=2*index+1;
    int r=2*index+2;
    int smallerIndex;
    if(l>=N)return;
    if(l==N-1){
      smallerIndex=l;
    }
    else if(l<N && data[l]<data[r]){
      smallerIndex=l;
    }     
    else if(r<N && data[r]<data[l]){
      smallerIndex=r;
    }
    if(data[smallerIndex]<data[index]){
      swap(index,smallerIndex);
      siftDown(smallerIndex);
    }
    return;
  }
  void GenerateSwaps() {
    for(int i=(N/2);i>=0;i--){
      siftDown(i);
    }
  }

 public:
  void Solve() {
    ReadData();
    GenerateSwaps();
    WriteResponse();
  }
};

int main() {
  std::ios_base::sync_with_stdio(false);
  HeapBuilder heap_builder;
  heap_builder.Solve();
  return 0;
}
