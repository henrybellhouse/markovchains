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

def p_transition(transition_dict):
    unique_channel_list = set(x for element in paths_list for x in element)
    p_transition = defaultdict(dict)
    for state in unique_channel_list:
        if state not in ['Conversion', 'Null']:
            counter = 0
            index = [i for i, s in enumerate(transition_dict) if state + '>' in s]
            for col in index:
                if transition_dict[list(transition_dict)[col]] > 0:
                    counter += transition_dict[list(transition_dict)[col]]
            for col in index:
                if transition_dict[list(transition_dict)[col]] > 0:
                    state_prob = float((transition_dict[list(transition_dict)[col]])) / float(counter)
                    p_transition[list(transition_dict)[col]] = state_prob

    return p_transition

p_transition = p_transition(transition_list)
