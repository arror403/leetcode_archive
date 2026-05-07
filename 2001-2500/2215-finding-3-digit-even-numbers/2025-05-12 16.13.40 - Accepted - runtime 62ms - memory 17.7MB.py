class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # p=permutations(digits, 3)
        # res=set()

        # for x in p:
        #     if x[0]==0 or x[2]%2==1:
        #         continue
        #     else:
        #         res.add(int(''.join(str(t) for t in x)))


        # return sorted(list(res))

        count = Counter(digits)
        result = []
        
        for num in range(100, 999, 2):  # Step by 2 to get only even numbers
            # Convert to string and check if we have all required digits
            num_str = str(num)
            num_counter = Counter(int(digit) for digit in num_str)
            
            # Check if we have enough occurrences of each digit
            valid = True
            for digit, freq in num_counter.items():
                if count[digit] < freq:
                    valid = False
                    break
            
            if valid:
                result.append(num)
                
        return result