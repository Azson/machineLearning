# include <cstdio>
# include <string>

using namespace  std;

class Solution {
public:
    /**
     * 
     * @param n int整型 
     * @param p int整型 
     * @param q int整型 
     * @return int整型
     */
    /*
    p>q
        必胜:1,2,...,q,...,p 
    p<q

    p=q
        必胜:1,2...,p,p+2,p+3,...,2p
        必败:p+1,2(p+1)
    */

	int Gameresults(int n, int p, int q) {
		if(n<=p)
			return 1;
		if(p>q)
			return 1;
		if(p<q)
			return -1;
		if(n%(p+1)==0)
			return -1;
		return 1;
    }
};