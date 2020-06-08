#include <iostream>
#include <utility>
#include <vector>
using namespace std;
typedef unsigned long long ull;

struct Answer
{
	size_t i, j, len;
};

Answer solvek(const string &s, const string &t, int k)
{
//	cout << "*** " << k << "| "<<endl;
	Answer fin = {0, 0, 0};
	int sLen = s.size();
	int tLen = t.size();
	ull prime1 = 1000000007;
	ull prime2 = 1000000033;
	ull multiplier1 = rand() % 1000000007;
	ull multiplier2 = ( rand() % 1000000033);
	if(multiplier1<30000)multiplier1+=30000;
	if(multiplier2<30000)multiplier2+=30000; 
//	cout<<"*** "<<multiplier1<<" "<<multiplier2<<" ***"<<endl;
	ull pows1[k + 1];
	ull pows2[k + 1];
	int m = 5003;
	vector<vector<pair<ull, int>>> hashTable(m);

	ull y1 = 1;
	ull y2 = 1;
	for (int i = 1; i <= k; i++)
	{
		y1 = (ull)((y1 * multiplier1) % prime1);
		y2 = (ull)((y2 * multiplier2) % prime2);
	}
	ull precompS1[sLen - k + 1];
	ull precompS2[sLen - k + 1];
	ull origHashS1 = 0;
	ull origHashS2 = 0;
	for (int i = sLen - 1; i >= sLen - k; i--)
	{
		origHashS1 = (ull)((origHashS1 * multiplier1 + s[i]) % prime1);
		origHashS2 = (ull)((origHashS2 * multiplier2 + s[i]) % prime2);
	}
	precompS1[sLen - k] = origHashS1;
	precompS2[sLen - k] = origHashS2;
	hashTable[origHashS1 % m].push_back(make_pair(origHashS1, sLen - k));
	hashTable[origHashS2 % m].push_back(make_pair(origHashS2, sLen - k));
//	cout<<sLen-k<<" "<<origHashS1<<" "<<origHashS2<<endl;
	for (int i = sLen - k - 1; i >= 0; i--)
	{
		precompS1[i] = (ull)((precompS1[i + 1] * multiplier1 + s[i] - s[i + k] * y1) % prime1);
		precompS2[i] = (ull)((precompS2[i + 1] * multiplier2 + s[i] - s[i + k] * y2) % prime2);
//		cout<<i<<" "<<precompS1[i]<<" "<<precompS2[i]<<endl;
		hashTable[precompS1[i] % m].push_back(make_pair(precompS1[i], i));
		hashTable[precompS2[i] % m].push_back(make_pair(precompS2[i], i));
	}
	//--------------------------- T ------------------------------
//	cout<<endl<<endl;
	ull precompT1[tLen - k + 1];
	ull precompT2[tLen - k + 1];
	ull origHashT1 = 0;
	ull origHashT2 = 0;
	for (int i = tLen - 1; i >= tLen - k; i--)
	{
		origHashT1 = (ull)((origHashT1 * multiplier1 + t[i]) % prime1);
		origHashT2 = (ull)((origHashT2 * multiplier2 + t[i]) % prime2);
	}
	
/*
	cout << "                  " <<tLen-k<<" ";
    cout<<"1:  "<<origHashT1<<" ";
    for(int q=0;q<hashTable[origHashT1%m].size();q++){
        cout<<" ( "<<hashTable[origHashT1%m][q].first<<" "<<hashTable[origHashT1%m][q].second<<" ) ";
    }
    cout<<"      2: "<<origHashT2<<" ";
    for(int q=0;q<hashTable[origHashT2%m].size();q++){
        cout<<" ( "<<hashTable[origHashT2%m][q].first<<" "<<hashTable[origHashT2%m][q].second<<" ) ";
    }
    cout<<endl;

*/
	precompT1[tLen - k] = origHashT1;
	precompT2[tLen - k] = origHashT2;
	for (int i = 0; i < hashTable[origHashT1 % m].size(); i++)
	{
		for (int j = 0; j < hashTable[origHashT2 % m].size(); j++)
		{

			if (hashTable[origHashT1 % m][i].second == hashTable[origHashT2 % m][j].second)
			{
				if (hashTable[origHashT1 % m][i].first == origHashT1 && hashTable[origHashT2 % m][j].first == origHashT2)
				{
					fin.i = hashTable[origHashT1 % m][i].second;
					fin.j = tLen - k;
					fin.len = k;
//					              cout << fin.i << " " << fin.j << " " << fin.len << " A" << endl;
					return fin;
				}
			}
		}
	}

	for (int i = tLen - k - 1; i >= 0; i--)
	{
		precompT1[i] = (ull)((precompT1[i + 1] * multiplier1 + t[i] - t[i + k] * y1) % prime1);
		precompT2[i] = (ull)((precompT2[i + 1] * multiplier2 + t[i] - t[i + k] * y2) % prime2);
/*		
		cout << "                  " <<i<<" ";
    	cout<<"1:  "<<precompT1[i]<<" ";
    	for(int q=0;q<hashTable[precompT1[i]%m].size();q++){
        	cout<<" ( "<<hashTable[precompT1[i]%m][q].first<<" "<<hashTable[precompT1[i]%m][q].second<<" ) ";
    	}
    	cout<<"      2: "<<precompT2[i]<<" ";
    	for(int q=0;q<hashTable[precompT2[i]%m].size();q++){
        	cout<<" ( "<<hashTable[precompT2[i]%m][q].first<<" "<<hashTable[precompT2[i]%m][q].second<<" ) ";
    	}
    	cout<<endl;
*/
		for (int a = 0; a < hashTable[precompT1[i] % m].size(); a++)
		{
			for (int b = 0; b < hashTable[precompT2[i] % m].size(); b++)
			{
				if (hashTable[precompT1[i] % m][a].second == hashTable[precompT2[i] % m][b].second)
				{
					if (hashTable[precompT1[i] % m][a].first == precompT1[i] && hashTable[precompT2[i] % m][b].first == precompT2[i])
					{
						fin.i = hashTable[precompT1[i] % m][a].second;
						fin.j = i;
						fin.len = k;
	//					cout << fin.i << " " << fin.j << " " << fin.len << " B" << endl;
						return fin;
					}
				}
			}
		}
	}
  //  cout << fin.i << " " << fin.j << " " << fin.len << " C" << endl;
	return fin;
}

int main()
{
	ios_base::sync_with_stdio(false), cin.tie(0);
	string s, t;
	while (cin >> s >> t)
	{
		int beg = 0;
		int end = min(s.size(), t.size()) + 1;
		int max = 0;
		bool works = true;
		Answer ans = {0, 0, 0};
		while (end - beg > 1)
		{
			int mid = (beg + end) / 2;
			Answer ansK = solvek(s, t, mid);
			if (ansK.len == 0)
			{
				end = mid;
			}
			else
			{
				if (ansK.len > max)
				{
					ans.i = ansK.i;
					ans.j = ansK.j;
					ans.len = ansK.len;
					max = ansK.len;
				}
				beg = mid;
			}
		}
		Answer ans2 = solvek(s, t, min(s.size(), t.size()));
		//   cout<<"*** "<<min(t.size(),s.size())<<endl;
		if (ans2.len != 0)
		{
			ans = ans2;
		}
		Answer one=solvek(s,t,1);
		if(ans.len==0){
			ans=one;
		}
		//		*/

		cout << ans.i << " " << ans.j << " " << ans.len << "\n";
	}
}

