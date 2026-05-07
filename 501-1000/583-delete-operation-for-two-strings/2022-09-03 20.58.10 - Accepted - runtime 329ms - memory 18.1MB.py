class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r=self.find_lcseque(word1,word2)
    
    
        return len(word1)+len(word2)-2*len(r)
    
    
    def find_lcseque(self, s1, s2):
        # 生成字符串長度加1的0矩陣，m用來保存對應位置匹配的結果
        m = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
        # d用來記錄轉移方向
        d = [[None for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

        for p1 in range(len(s1)):
            for p2 in range(len(s2)):
                if s1[p1] == s2[p2]:  # 字符匹配成功，則該位置的值爲左上方的值加1
                    m[p1 + 1][p2 + 1] = m[p1][p2] + 1
                    d[p1 + 1][p2 + 1] = 'ok'
                elif m[p1 + 1][p2] > m[p1][p2 + 1]:  # 左值大於上值，則該位置的值爲左值，並標記回溯時的方向
                    m[p1 + 1][p2 + 1] = m[p1 + 1][p2]
                    d[p1 + 1][p2 + 1] = 'left'
                else:  # 上值大於左值，則該位置的值爲上值，並標記方向up
                    m[p1 + 1][p2 + 1] = m[p1][p2 + 1]
                    d[p1 + 1][p2 + 1] = 'up'
        (p1, p2) = (len(s1), len(s2))
        # print(numpy.array(d))
        s = []
        while m[p1][p2]:  # 不爲None時
            c = d[p1][p2]
            if c == 'ok':  # 匹配成功，插入該字符，並向左上角找下一個
                s.append(s1[p1 - 1])
                p1 -= 1
                p2 -= 1
            if c == 'left':  # 根據標記，向左找下一個
                p2 -= 1
            if c == 'up':  # 根據標記，向上找下一個
                p1 -= 1
        s.reverse()
        return ''.join(s)