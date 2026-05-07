class Solution:
    def reformatNumber(self, number: str) -> str:
        # number.remove(' ')
        # number.remove('-')

        return re.sub('(...?(?=..))', r'\1-', re.sub('\D', '', number))