import pandas as pd

def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    sessions = {}
    res=[]
    
    for _,row in customer_transactions.iterrows():
        customerId = row['customer_id']
        
        if customerId not in sessions:
            sessions[customerId] = [0, 0, set(), customerId]
        
        if row['transaction_type'] == 'purchase':
            sessions[customerId][0] += 1
        
        elif row['transaction_type'] == 'refund':
            sessions[customerId][1] += 1
 
        sessions[customerId][2].add(row['transaction_date'])
    
    for stats in sessions.values():
        purchase_count, refund_count, timestamps, customerId = stats

        datetime_timestamps=[pd.to_datetime(x) for x in timestamps]
        datetime_timestamps.sort()
        duration_day = (datetime_timestamps[-1] - datetime_timestamps[0]).total_seconds() / 86400
        
        if duration_day >= 30:     
            refund_to_purchase_ratio = refund_count / (refund_count + purchase_count)
            if refund_to_purchase_ratio<0.2 and purchase_count>=3:
                res.append(customerId)
      

    return pd.DataFrame({'customer_id': res}).sort_values(by=['customer_id'])
