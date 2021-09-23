#include <iostream>
#include <set>
using namespace std;

int main()
{
    int L, Q;
    cin >> L >> Q;

    set<int> st;
    st.insert(0);
    st.insert(L);
    for (int i = 0; i < Q; i++)
    {
        int ci, xi;
        cin >> ci >> xi;
        if (ci == 1)
        {
            st.insert(xi);
        }
        else
        {
            auto it = st.lower_bound(xi);
            cout << *it - *prev(it) << endl;
        }
    }
}
