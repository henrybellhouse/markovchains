# Markov Attribution
Markov Chains can help to solve the Channel Attribution problem by modelling the customer journey as a sequence of events, where each event corresponds to a customer interaction with a marketing channel. The probability of a customer transitioning from one channel to another can then be estimated based on historical data. By analysing these transition probabilities, it is possible to determine which channels are most effective at driving conversions.

Markov Chains are a type of stochastic model that represent a sequence of events, where the probability of each event depends only on the state of the previous event. Markov Chains can be used to model systems where the future state depends only on the present state, and not on any past states. To motivate this work and reinforce my statistical knowledge, I drew from Stanford University STAT217 class notes, which can be found in the Resource section at the end of this walkthrough.

# Dataset

This analysis draws from public eCommerce data that is 'clean', with approximately 600,000 touchpoints for 250,000 unique customers (the field 'cookie' is used as a unique identifier). This dataset also has a timestamp column to ascertain the chronological order of touchpoints in a particular customer journey.
Additionally, the field 'interaction' helps us discriminate between impressions (non-conversion events) and conversions so we can extend our analysis to customers that abandoned their journey or have failed to convert. There is a boolean data field named 'conversion', which = 1 if the touchpoint is a conversion event and = 0 if not (is an impression). Of less importance in this analysis is 'conversion_value', which holds the numerical value of the conversion event. In eCommerce analysis, this is the 'Basket Size' or 'Transaction Revenue'.

The field 'channel' lists strings for all possible marketing channels a customer can come into contact with in their journey. The list is: 'Facebook', 'Instagram', 'Online Display', 'Online Video' and 'Paid Search'.

# Pre-Processing

I took important steps in pre-processing (found in processing.py), and it is worth the mention that this dataset is more idealised when compared to real-world industry datasets. However, what needed to be done was import my .csv dataset into a Pandas DataFrame for subsequent manipulation with the package. Using the os package, this was relatively simple and I would encourage other practitioners to investigate use cases of this package. I also converted the 'time' field using pd.to_datetime so that time series analysis was as intuitive as possible. I sorted values in descending order by 'cookie' and ascending order by this same 'time' field, effectively grouping the dataset by each customer with a ranked list from their first touchpoint to their last. The final step was to add the 'order' field which we append to the dataset to track the order of events in a customer journey.

Specific pre-processing was needed to model the data with Markov Chains. Converting from a 'long-form' dataset to 'wide-form' permitted me to remove duplicate values from the first column. Here, this meant we had one row per customer; their touchpoints are stored as an ordered list in a single row, too. This itself was an extremely difficult challenge and I drew from similar analysis that had been done that contained a similar manipulation step.


# Map of Transitions

One valuable function I wrote for this analysis is a 'map' of all possible transitions from one channel to the next. The output of the function is a dictionary containing all possible iterations seen in the data. Being able to count the number of times a given transition occurs is the foundation to calculating the probability of a given transition.

Once this was successful, we needed a function for transition probabilities. Mathematically, this is counting the specific instances of one particular transition as the numerator, with the numerical count of  observed transitions as the denominator.

# Matrix Transformation and Removal Effects

Removal effects in Markov chains refer to the changes in the probability distribution of the states in the chain that occur when a particular state is removed. The removal effect of a state is the difference between the probability of being in each state with the state present and the probability of being in each state with the state removed. These effects are useful in understanding the importance of particular states in the chain, as well as in making predictions about future states.

Examining the removal effects of all states in the chain will give us insights into which states are most influential in determining the long-term behaviour of the chain. In this context, we investigate which states are driving conversions (the long-term behaviour of a given customer journey).

# Conclusion

Having computed the Removal Effects, we are able to conclude the approach and ascertain the number of credits to be assigned to each marketing channel. As we can see, Facebook is assigned the highest number of credits for this dataset. If this data is representative of the entire user base then Facebook would be deemed the most valuable touchpoint for a given journey. Furthermore, normalising these credit indicates that, if we take a converted customer journey at random, we expect that more than half of the assigned credit to be attributed to Facebook and Paid Search, alone. The expected credit for Facebook is equal to the combined credit that we expect for Online Display and Online Video.

Building a statistical approach with Markov Chains is more objective and empirical compared to heuristic models, which often rely on predefined rules or assumptions. This should give Marketing and Growth teams insight into which channels are driving conversions most effectively, and can serve as evidence to support changes in their marketing mix.

# Resources

[Stanford STAT217 Lecture Note](https://web.stanford.edu/class/stat217/New12.pdf)
