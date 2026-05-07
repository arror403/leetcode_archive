import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    paid_user = user_activity[user_activity['activity_type'] == 'paid'].groupby('user_id')['activity_duration'].mean().apply(lambda x: round(x+0.00001, 2)).reset_index(name = 'paid_avg_duration').round(2)

    free_user = user_activity[user_activity['activity_type'] == 'free_trial'].groupby('user_id')['activity_duration'].mean().apply(lambda x: round(x, 2)).reset_index(name = 'trial_avg_duration').round(2)

    Result = pd.merge(paid_user, free_user, on = 'user_id')[['user_id','trial_avg_duration', 'paid_avg_duration']].sort_values(by = 'user_id', ascending = True)


    return Result
    # m=zip(user_activity["user_id"],user_activity["activity_type"],user_activity["activity_duration"])
    # pu=defaultdict(list)
    # fu=defaultdict(list)

    # for u,t,d in m:
    #     if t=="free_trial":
    #         fu[u].append(d)
    #     elif t=="paid":
    #         pu[u].append(d)

    # users=sorted(list(set(user_activity["user_id"])))
    # pd=[]
    # fd=[]
    
    # for u in users:
    #     pd.append(sum(pu[u])/len(pu[u]))
    #     fd.append(sum(fu[u])/len(fu[u]))
        

    # return pd.DataFrame({"user_id":users, "trial_avg_duration":fd, "paid_avg_duration":pd})