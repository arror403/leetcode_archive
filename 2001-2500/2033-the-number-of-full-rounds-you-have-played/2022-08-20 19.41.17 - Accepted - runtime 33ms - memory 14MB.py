class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        h1,m1=int(loginTime[0:2]),int(loginTime[3:5])
        h2,m2=int(logoutTime[0:2]),int(logoutTime[3:5])
        
        if 0<=(h2*60+m2)-(h1*60+m1)<15: return 0
        
        if m1>0 and m1<=15:
            m1=15
        elif m1>15 and m1<=30:
            m1=30
        elif m1>30 and m1<=45:
            m1=45
        elif m1>45:
            h1+=1
            m1=0
            
        if m2>=0 and m2<15:
            m2=0
        elif m2>=15 and m2<30:
            m2=15
        elif m2>=30 and m2<45:
            m2=30
        else:
            m2=45
            
        print(h1,m1)
        print(h2,m2)
            
        if (h1*60+m1)>(h2*60+m2):
            return (1440-(h1*60+m1)+(h2*60+m2))//15
        
        return ((h2*60+m2)-(h1*60+m1))//15