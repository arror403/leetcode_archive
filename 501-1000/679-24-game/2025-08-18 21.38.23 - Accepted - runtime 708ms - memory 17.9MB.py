class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ops = ['+', '-', '*', '/']
        
        for perm in permutations(cards):
            a, b, c, d = perm
            for op1 in ops:
                for op2 in ops:
                    for op3 in ops:
                        expressions = [
                            f"(({a} {op1} {b}) {op2} {c}) {op3} {d}",      # ((a op b) op c) op d
                            f"({a} {op1} ({b} {op2} {c})) {op3} {d}",      # (a op (b op c)) op d
                            f"({a} {op1} {b}) {op2} ({c} {op3} {d})",      # (a op b) op (c op d)
                            f"{a} {op1} (({b} {op2} {c}) {op3} {d})",      # a op ((b op c) op d)
                            f"{a} {op1} ({b} {op2} ({c} {op3} {d}))"       # a op (b op (c op d))
                        ]
                        
                        for expr in expressions:
                            try:
                                if abs(eval(expr) - 24) < 1e-6:
                                    return True
                            except (ZeroDivisionError, ValueError):
                                continue

        return False