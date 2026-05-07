class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        return Counter(w for w in words if w not in banned).most_common(1)[0][0]

    # \w
    # Matches Unicode word characters; this includes all Unicode alphanumeric characters (as defined by str.isalnum()), as well as the underscore (_).
    # Matches [a-zA-Z0-9_] if the ASCII flag is used.