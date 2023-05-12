def matrix(paths_list, transition_probabilities):
    matrix = pd.DataFrame()
    unique_channel_list = set(x for element in paths_list for x in element)

    for channel in unique_channel_list:
        matrix[channel] = 0.00
        matrix.loc[channel] = 0.00
        matrix.loc[channel][channel] = 1.0 if channel in ['Conversion', 'Null'] else 0.0

    for key, value in transition_probabilities.items():
        origin, destination = key.split('>')
        matrix.at[origin, destination] = value

    return matrix

matrix = matrix(paths_list, p_transition)
