#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    const int MOD = 998244353;
    vector<int> dp(9, 1);
    for (int i = 0; i < N - 1; i++)
    {
        vector<int> ndp(9);
        for (int j = 0; j < 9; j++)
        {
            if (j > 0)
            {
                ndp[j] = (ndp[j] + dp[j - 1]) % MOD;
            }
            ndp[j] = (ndp[j] + dp[j]) % MOD;
            if (j < 9)
            {
                ndp[j] = (ndp[j] + dp[j + 1]) % MOD;
            }
        }
        for (int j = 0; j < 9; j++)
        {
            dp[j] = ndp[j] % MOD;
        }
    }

    int ans = 0;
    for (int i = 0; i < 9; i++)
    {
        ans += dp[i];
        ans %= MOD;
    }
    cout << ans << endl;
}
