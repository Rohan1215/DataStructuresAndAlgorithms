#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Query {
    string type, s;
    int ind;
};

class QueryProcessor {
    int bucket_count;
    // store all strings in one vector
    vector<vector<string>> elems;
    int hash_func(const string& s) const {
        static const int multiplier = 263;
        static const int prime = 1000000007;
        unsigned long long hash = 0;
        for (int i = s.size() - 1; i >= 0; --i)
            hash = (hash * multiplier + s[i]) % prime;
        return hash % bucket_count;
    }

public:
    explicit QueryProcessor(int bc){
        bucket_count=bc;
        elems.resize(bucket_count);
    }

    Query readQuery() const {
        Query query;
        cin >> query.type;
        if (query.type != "check")
            cin >> query.s;
        else
            cin >> query.ind;
        return query;
    }

    void writeSearchResult(bool was_found) const {
        cout << (was_found ? "yes\n" : "no\n");
    }
    vector<string>::iterator find(int index, string val){
        for(vector<string>::iterator it =elems[index].begin();it!=elems[index].end();it++){
            if(*it==val){
                return it;
            }
        }
        return elems[index].end();
    }
    void processQuery(const Query& query) {
        if (query.type == "check") {
            for(int i=elems[query.ind].size()-1;i>=0;i--){
                cout<<elems[query.ind][i]<<" ";
            }
            cout<<endl;
        } 
        else{
            int hashed=hash_func(query.s);
            vector<string>::iterator there=find(hashed,query.s);
            if(query.type=="add"){
                if(there==elems[hashed].end())  elems[hashed].push_back(query.s);
            }
            else if(query.type=="del"){
                if(there!=elems[hashed].end())  elems[hashed].erase(there);
            }
            else{
                writeSearchResult(there!=elems[hashed].end());
            }
        }
    }

    void processQueries() {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i)
            processQuery(readQuery());
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    int bucket_count;
    cin >> bucket_count;
    QueryProcessor proc(bucket_count);
    proc.processQueries();
    return 0;
}
