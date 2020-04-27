#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
using namespace std;

class JobQueue {
 private:
  int N;
  int M;
  int currentJob=0;
  long long currentTime=0;
  int jobs[100000];
  priority_queue<int,vector<int>,greater<int>> threads;
  priority_queue<pair<long long,int>,vector<pair<long long,int>>,greater<pair<long long,int>>> jobsRemaining;
  int assigned_workers[100000];
  long long start_times[100000];
  void WriteResponse() const {
    for (int i = 0; i < M; ++i) {
      cout << assigned_workers[i] << " " << start_times[i] << "\n";
    }
  }
  int getJobs(){
      int jobTime=jobs[currentJob];
      currentJob++;
      return jobTime;

  }
  void ReadData() {
    //ifstream in ("prob2input.txt");
    cin >> N >> M;
    for(int i = 0; i < M; ++i)
      cin >> jobs[i];
    //in.close();
    //cout<<"INPUT READ"<<endl;
  }

  void AssignJobs() {
    for(int i=0;i<N;i++) threads.push(i);
    //*
    while(currentJob<M){
        if(!jobsRemaining.empty()){
            long long newTime=jobsRemaining.top().first;
            while((!jobsRemaining.empty()) && jobsRemaining.top().first==newTime){
                threads.push(jobsRemaining.top().second);
                jobsRemaining.pop();
            }
            currentTime=newTime;
        }
        while(!threads.empty()){
            if(currentJob>=M) return;
            int worker=threads.top();
            assigned_workers[currentJob]=worker;
            threads.pop();
            start_times[currentJob]=currentTime;
            jobsRemaining.push(make_pair(currentTime+getJobs(),worker));
        }
    }
    //*/
  }

 public:
  void Solve() {
    ReadData();
    AssignJobs();
    WriteResponse();
  }
};

int main() {
  std::ios_base::sync_with_stdio(false);
  JobQueue job_queue;
  job_queue.Solve();
  return 0;
}
