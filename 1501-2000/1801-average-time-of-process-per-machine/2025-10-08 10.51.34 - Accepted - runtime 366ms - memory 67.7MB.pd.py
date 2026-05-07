import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # m=set(activity['machine_id'])
    # p=set(activity['process_id'])
    # p=defaultdict(defaultdict(int))

#     for _,r in iterrows(activity):
#         t=r['timestamp']
#         if r['activity_type']=='end':
#             t*=-1
#         if r['process_id'] in p[r['machine_id']]:
#             p[r['machine_id']][r['process_id']]+=t
#         else:
#             p[r['machine_id']][r['process_id']]=t

#     print(p)

#     return pd.DataFrame()

# import pandas as pd

# def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
        p = activity.pivot(index=["machine_id", "process_id"], columns='activity_type', values='timestamp')
        p['processing_time'] = p['end'] - p['start']
        return p.groupby('machine_id').processing_time.mean().round(3).reset_index()