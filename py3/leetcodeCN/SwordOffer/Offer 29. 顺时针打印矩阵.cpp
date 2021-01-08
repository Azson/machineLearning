class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n;
        if (m > 0) n = matrix[0].size();
        int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1}, x, y, tx, ty;
        x = y = 0;
        vector<int> ans;
        tx = (n-1)/2, ty = m/2;
        map<int, bool> mp;
        for (int i = 0;i < (m+1)/2;i++) {
            for (int j = 0;j < 4;j++) {
                while (true) {
                    if (mp[y*100+x]) {
                        return ans;
                    }
                    //printf("%d %d\n", y, x);
                    ans.push_back(matrix[y][x]);
                    
                    mp[y*100+x] = true;
                    x += dx[j];
                    y += dy[j];
                    if (!(y >= i && y < m-i && x >= i && x < n-i) || 
                        (j == 3 && y == i)) {
                        x -= dx[j];
                        y -= dy[j];
                        x += dx[(j+1)%4];
                        y += dy[(j+1)%4];
                        if (!(y >= i && y < m-i && x >= i && x < n-i) || 
                            (j == 3 && y == i)) {
                            return ans;
                         }
                        break;
                    }
                    
                }
            }
        }
        return ans;
    }
};