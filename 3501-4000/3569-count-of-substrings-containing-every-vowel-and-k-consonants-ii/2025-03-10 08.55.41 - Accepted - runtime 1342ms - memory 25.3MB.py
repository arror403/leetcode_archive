class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:   
        def isVowel(ch):
            return ch in "aeiou"

        n=len(word)
        vowels=defaultdict(int)
        consonantCount=result=0

        # Precompute next consonant positions
        nextConsonant=[0]*n
        lastConsonant=n
        for i in range(n-1,-1,-1):
            nextConsonant[i]=lastConsonant
            if not isVowel(word[i]):
                lastConsonant=i
        

        # Sliding window
        left = right = 0
        while right<n:
            # Expand window
            if isVowel(word[right]):
                vowels[word[right]]+=1
            else:
                consonantCount+=1
            

            # Shrink window if too many consonants
            while (left<=right and consonantCount>k):
                if isVowel(word[left]):
                    vowels[word[left]]-=1
                    if vowels[word[left]]==0:
                        del vowels[word[left]]
                else:
                    consonantCount-=1
                
                left+=1
            

            # Count valid substrings
            while (left<right and len(vowels)==5 and consonantCount==k):
                result+=(nextConsonant[right]-right)
                if isVowel(word[left]):
                    vowels[word[left]]-=1
                    if vowels[word[left]]==0:
                        del vowels[word[left]]
                else:
                    consonantCount-=1

                left+=1

            right+=1


        return result