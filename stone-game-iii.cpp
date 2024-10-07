class Solution
{
public:
    static const int N = 5e4 + 5;
    int dp[N][2];

    int solve(int index, bool turn, vector<int> &stoneValue)
    {
        if (index >= stoneValue.size())
        {
            return 0;
        }
        if (dp[index][turn] != -1)
        {
            return dp[index][turn];
        }
        if (!turn)
        {
            int s = 0;
            dp[index][turn] = -1e8;
            for (int i = 0; i < 3 && i + index < stoneValue.size(); i++)
            {
                s += stoneValue[index + i];
                dp[index][turn] = max(dp[index][turn], solve(index + i + 1, 1 - turn, stoneValue) + s);
            }
        }
        else
        {
            int s = 0;
            dp[index][turn] = 1e8;
            for (int i = 0; i < 3 && i + index < stoneValue.size(); i++)
            {
                s += stoneValue[index + i];
                dp[index][turn] = min(dp[index][turn], solve(index + i + 1, 1 - turn, stoneValue) - s);
            }
        }

        return dp[index][turn];
    }

    string stoneGameIII(vector<int> &stoneValue)
    {

        memset(dp, -1, sizeof dp);

        int ans = solve(0, 0, stoneValue);

        if (ans > 0)
            return "Alice";
        if (ans < 0)
            return "Bob";
        return "Tie";
    }
};