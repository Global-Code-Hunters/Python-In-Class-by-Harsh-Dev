CHECK WEATHER THE GIVEN STRING IS PALINGDROME OR NOT USING RECURSION

-------------------------------      C++  -------------------------------------------

```.cpp

#include<bits/stdc++.h>
using namespace std;
bool check_for_even(string s)
{
    stack<char>st;
    int n=s.length();
    int i=0;
    for(i=0;i<n/2;i++)
    {
        st.push(s[i]);
    }
    while(!st.empty())
    {
        if(st.top()!=s[i])return false;
        // cout<<st.top()<<" "<<s[i]<<endl;
        i++;
        st.pop();
    }
    return true;
}
bool check_for_odd(string s)
{
    stack<char>st;
    int n=s.length();
    int i=0;
    for(i=0;i<n/2;i++)
    {
        st.push(s[i]);
    }
    i++;
    while(!st.empty())
    {
        if(st.top()!=s[i])return false;
        // cout<<st.top()<<" ";
        i++;
        st.pop();
    }
    return true;
}
int main()
{
    string s;
    cin>>s;
    int n=s.length();
    if(n%2==0)
    {
        cout<<check_for_even(s)<<endl;
    }
    else
        cout<<check_for_odd(s)<<endl;
return 0;
}




```


-------------------------------------   PYTHON --------------------------------------

<H3> USING RECUSION: </H3>

```.PY

s=input()
def check(s):
    if len(s)==0 or len(s)==1:
        return "YES"
    else:
        if s[0]==s[-1]:
            s=s[1:-1]
            return check(s)
        else:
            return "NO"
    

print(check(s))

```
