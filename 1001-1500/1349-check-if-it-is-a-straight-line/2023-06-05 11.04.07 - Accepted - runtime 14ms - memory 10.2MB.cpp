class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        if (coordinates[0][0] == coordinates[1][0]) {
            for (auto i : coordinates) {
                if (i[0] == coordinates[0][0]) continue;
                else return false;
            }
            return true;
        } else {
            double m = (coordinates[0][1] - coordinates[1][1]) / (double)(coordinates[0][0] - coordinates[1][0]);
            double b = coordinates[0][1] - m * coordinates[0][0];

            for (auto i : coordinates) {
                if (i[0] * m + b == i[1]) continue;
                else return false;
            }
            return true;
        }
    }
};