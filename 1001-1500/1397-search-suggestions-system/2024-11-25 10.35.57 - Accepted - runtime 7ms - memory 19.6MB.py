class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, p, i = [], '', 0

        for c in searchWord:
            p+=c
            i=bisect_left(products, p , i)
            res.append([w for w in products[i:i+3] if w.startswith(p)])


        return res