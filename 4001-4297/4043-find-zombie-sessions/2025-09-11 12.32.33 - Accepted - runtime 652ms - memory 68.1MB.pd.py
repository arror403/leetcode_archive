import pandas as pd

def find_zombie_sessions(app_events: pd.DataFrame) -> pd.DataFrame:
    sessions = {}
    
    for _, row in app_events.iterrows():
        session_id = row['session_id']
        
        # Initialize session if not exists
        if session_id not in sessions:
            sessions[session_id] = [0, 0, [], row['user_id'], False]
        
        # Count scroll events
        if row['event_type'] == 'scroll':
            sessions[session_id][0] += 1
        
        # Count click events
        elif row['event_type'] == 'click':
            sessions[session_id][1] += 1
        
        # Check for purchases
        elif row['event_type'] == 'purchase':
            sessions[session_id][4] = True
        
        # Add timestamp to track session duration
        sessions[session_id][2].append(row['event_timestamp'])
    
    # Find zombie sessions
    zombie_sessions = []
    
    for session_id, stats in sessions.items():
        scroll_count, click_count, timestamps, user_id, has_purchase = stats

        datetime_timestamps=[pd.to_datetime(ts) for ts in timestamps]
        # # Calculate session duration in minutes
        datetime_timestamps.sort()
        duration_minutes = (datetime_timestamps[-1] - datetime_timestamps[0]).total_seconds() / 60
        
        # Check all zombie session criteria
        if (duration_minutes > 30 and           # Duration > 30 minutes
            scroll_count >= 5 and              # At least 5 scroll events
            not has_purchase):                 # No purchases
            
            # Calculate click-to-scroll ratio
            click_to_scroll_ratio = click_count / scroll_count if scroll_count > 0 else 0
            
            # Check if click-to-scroll ratio is less than 0.20
            if click_to_scroll_ratio < 0.20:
                zombie_sessions.append({
                    'session_id': session_id,
                    'user_id': user_id,
                    'session_duration_minutes': int(duration_minutes),
                    'scroll_count': scroll_count
                })
    

    return pd.DataFrame(zombie_sessions).sort_values(['scroll_count', 'session_id'], 
                        ascending=[False, True]).reset_index(drop=True)




    # d={}

    # for _,r in app_events.iterrows():
    #     if pd.isna(r['event_value']):
    #         if r['session_id'] not in d:
    #             d[r['session_id']]=[0, 0, [], r['user_id']]

    #     if r['event_type']=='scroll':
    #         d[r['session_id']][0]+=1

    #     if r['event_type']=='click':
    #         d[r['session_id']][1]+=1

    #     d[r['session_id']][2].append(r['event_timestamp'])


    # print(d)

    # return pd.DataFrame()