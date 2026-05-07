import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    def is_valid_email(email: str) -> bool:
        if not isinstance(email, str):
            return False
            
        if email.count('@') != 1:
            return False
            
        local_part, domain = email.split('@')
        
        if not local_part or not local_part.isalnum():
            return False
            
        if not domain.endswith('.com'):
            return False

        return True
    
    valid_mask = users['email'].apply(is_valid_email)
    
    result = users[valid_mask].sort_values('user_id')
    
    
    return result



    # res=[]
    # for i,m in zip(user('user_id'), user['email']):
    #     if m.count('@')!=1: continue

    #     f=1
    #     for j in range(m.index('@')):
    #         if not(j.isalnum() or j=='_'):
    #             f=0
    #             break

    #     if (not m.endswith('.com')): f=0
        
    #     if f: res.append([i,m])
