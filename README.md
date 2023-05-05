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

One valuable function I wrote for this analysis is a 'map' of all possible transitions from one channel to the next. The output of the function (found in transition.py) is a dictionary containing all possible iterations seen in the data. Being able to count the number of times a given transition occurs is the foundation to calculating the probability of a given transition.

Once this was successful, we needed a function for transition probabilities. Mathematically, this is counting the specific instances of one particular transition as the numerator, with the numerical count of  observed transitions as the denominator.

# Resources

[Stanford STAT217 Lecture Note on Markov Chains](https://web.stanford.edu/class/stat217/New12.pdf)
