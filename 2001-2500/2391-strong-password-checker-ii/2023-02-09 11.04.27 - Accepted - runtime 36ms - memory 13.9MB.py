class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        m="!@#$%^&*()-+"
        if len(password)<8: return False
        b=False
        for i in password:
            if i.islower():
                b=True
                break
        if b==False: return False
        b=False
        for i in password:
            if i.isupper():
                b=True
                break
        if b==False: return False
        b=False
        for i in password:
            if i.isdigit():
                b=True
                break
        if b==False: return False
        b=False
        for i in password:
            if i in m:
                b=True
                break
        if b==False: return False

        for i in range(len(password)-1):
            if password[i]==password[i+1]:
                return False

        return True