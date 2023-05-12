def markov_chain_allocations(removal_effects, conversion_total):
    re_sum = np.sum(list(removal_effects.values()))

    return {k: (v / re_sum) * conversion_total for k, v in removal_effects.items()}

attribution = markov_chain_allocations(removal_effects_dict, conversion_total)

print(attribution)

attribution = pd.Series(attribution).sort_values()
print(attribution)

(attribution / sum(attribution)).apply('{:.0%}'.format)
