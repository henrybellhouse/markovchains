# Possible Transitions
paths_list = df_paths['path']

def transition(paths_list):
    unique_channel_list = set(x for element in paths_list for x in element)
    transition = {x + '>' + y: 0 for x in unique_channel_list for y in unique_channel_list}

    for possible_state in unique_channel_list:
        if possible_state not in ['Conversion', 'Null']:
            for user_path in paths_list:
                if possible_state in user_path:
                    indices = [i for i, s in enumerate(user_path) if possible_state in s]
                    for col in indices:
                        transition[user_path[col] + '>' + user_path[col + 1]] += 1

    return transition

transition_list = transition(paths_list)
