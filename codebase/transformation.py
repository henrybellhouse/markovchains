# Markov Chain-specific Pre-Processing
df_paths = df.groupby('cookie')['channel'].aggregate(
    lambda x: x.unique().tolist()).reset_index()

df_last_interaction = df.drop_duplicates('cookie', keep='last')[['cookie', 'conversion']]
df_paths = pd.merge(df_paths, df_last_interaction, how='left', on='cookie')

df_paths['path'] = np.where(df_paths['conversion'] == 0,
                ['Start, '] + df_paths['channel'].apply(', '.join) + [', Null'],
                ['Start, '] + df_paths['channel'].apply(', '.join) + [', Conversion'])


df_paths['path'] = df_paths['path'].str.split(', ')

df_paths = df_paths[['cookie', 'path']]
df_paths.head()
