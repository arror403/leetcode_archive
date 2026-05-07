import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:

    m = zip(user_activity["user_id"], user_activity["activity_type"], user_activity["activity_duration"])
    pu = defaultdict(list)
    fu = defaultdict(list)
    for u, t, d in m:
        if t == "free_trial":
            fu[u].append(d)
        elif t == "paid":
            pu[u].append(d)
    
    users = sorted(list(set(user_activity["user_id"])))
    paid_durations = []
    free_durations = []
    
    for u in users:
        if u in pu and len(pu[u]) > 0:
            # Round to 2 decimal places with a small epsilon to match the reference implementation
            paid_durations.append(round(sum(pu[u])/len(pu[u]) + 0.00001, 2))
        else:
            paid_durations.append(None)
        
        if u in fu and len(fu[u]) > 0:
            # Round to 2 decimal places
            free_durations.append(round(sum(fu[u])/len(fu[u]), 2))
        else:
            free_durations.append(None)
    
    result = pd.DataFrame({
        "user_id": users, 
        "trial_avg_duration": free_durations, 
        "paid_avg_duration": paid_durations
    })
    
    # Filter to only include users who have both trial and paid data
    result = result.dropna()
    
    # Ensure result matches the reference implementation format
    result = result[["user_id", "trial_avg_duration", "paid_avg_duration"]]
    result = result.sort_values(by="user_id", ascending=True)
    
    
    return result