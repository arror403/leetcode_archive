class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        # total will contain total sum of sender's words                   
        total = {}
        max_name = ''
        max_value = 0
        
        for i in range(len(senders)):
            # get num of words in message             
            words_num = len(messages[i].split(' '))
            
            # if total contain sender's name
            # we add words_num to its value    
            # else add new key              
            if total.get(senders[i], None):
                total[senders[i]] += words_num
            else:
                total[senders[i]] = words_num
                
            # if max_num of words is equal to sender's total words num
            # and max_name is less then sender's name we change max_name        
            if total[senders[i]]==max_value and max_name<senders[i]:
                max_name = senders[i]
            
            # if sender's total words num is greater then current max
            # we save its name and num of words          
            elif total[senders[i]]>max_value:
                max_value = total[senders[i]]
                max_name = senders[i]
        return max_name