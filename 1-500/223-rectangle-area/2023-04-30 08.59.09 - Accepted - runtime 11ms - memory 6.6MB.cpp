class Solution {
public:
    int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        std::vector<int> r1 = {ax1, ax2, bx1, bx2};
        std::vector<int> r2 = {ay1, ay2, by1, by2};
        std::sort(r1.begin(), r1.end());
        std::sort(r2.begin(), r2.end());
        std::vector<int> rec1 = {ax1, ay1, ax2, ay2};
        std::vector<int> rec2 = {bx1, by1, bx2, by2};
        if (isRectangleOverlap(rec1, rec2)) {
            return std::abs((ax1 - ax2) * (ay1 - ay2)) + std::abs((bx1 - bx2) * (by1 - by2)) - std::abs((r1[1] - r1[2]) * (r2[1] - r2[2]));
        } else {
            return std::abs((ax1 - ax2) * (ay1 - ay2)) + std::abs((bx1 - bx2) * (by1 - by2));
        }
    }

    bool isRectangleOverlap(const std::vector<int>& rec1, const std::vector<int>& rec2) {
        bool widthIsPositive = std::min(rec1[2], rec2[2]) > std::max(rec1[0], rec2[0]);
        bool heightIsPositive = std::min(rec1[3], rec2[3]) > std::max(rec1[1], rec2[1]);
        return (widthIsPositive && heightIsPositive);
    }
};