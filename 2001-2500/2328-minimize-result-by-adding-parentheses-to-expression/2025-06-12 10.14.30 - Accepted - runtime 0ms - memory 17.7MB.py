class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split('+')
        min_value = inf
        best_result = ''
        
        for i in range(len(left)):
            for j in range(1, len(right) + 1):
                # Calculate components directly
                left_mult = int(left[:i]) if i > 0 else 1
                left_add = int(left[i:])
                right_add = int(right[:j])
                right_mult = int(right[j:]) if j < len(right) else 1
                
                # Calculate: left_mult * (left_add + right_add) * right_mult
                value = left_mult * (left_add + right_add) * right_mult
                
                if value < min_value:
                    min_value = value
                    best_result = f"{left[:i]}({left[i:]}+{right[:j]}){right[j:]}"
        
        return best_result