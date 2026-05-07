class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        seen=set()

        for f in sorted(folder, key=len):
            if not any(f[i]=='/' and f[:i] in seen for i in range(2, len(f))):
                seen.add(f)


        return list(seen)