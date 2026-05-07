class Solution:
    def interpret(self, command: str) -> str:
        b=[]
        for i in range(0,len(command)):
            if((command[i]=='(')&((i+1)<len(command))):
                if(command[i+1]==')'):
                    b.append('o')    
            elif command[i]=='G':
                b.append('G')
            elif command[i]=='a':
                b.append('a')                 
            elif command[i]=='l':
                b.append('l')
        b=''.join(b)
        
        return b