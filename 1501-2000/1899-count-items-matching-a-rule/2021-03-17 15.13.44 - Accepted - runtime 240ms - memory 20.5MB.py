class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        b=0
        if ruleKey=="type": 
            key=0
        
        if ruleKey=="color": 
            key=1
        
        if ruleKey=="name": 
            key=2
            
        for i in range(0,len(items)):
            
            if(items[i][key]==ruleValue):
                b+=1
                
        return b