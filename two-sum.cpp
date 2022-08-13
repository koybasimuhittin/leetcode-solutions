#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define f1 first
#define s2 second
#define pb push_back
#define mp make_pair
#define int long long
#define fri(a) freopen(a,"r",stdin);
#define fro(a) freopen(a,"w",stdout);
const int N=1e6+5;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>ans;
        map<int, int> mp;
        for(int i=0;i<nums.size();i++){
            mp[nums[i]]=i;
        }
        for(int i=0;i<nums.size();i++){
            if(mp.count(target-nums[i]) && i!=mp[target-nums[i]]){
                ans.push_back(mp[target-nums[i]]);
                ans.push_back(i);
                break;
            }
        }
        return ans;
    }
};

int main(){
	
	return 0;
}