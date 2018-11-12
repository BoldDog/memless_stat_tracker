# memless_stat_tracker
A lightweight python class that can track basic stats (mean, STD, sum of squares) ongoing without storing any data.


The script contains a single class which is initialised with a single number, and a string flag to indicate which negative-handler to use.
The script calculates the mean, standard deviation, sum of squares, number of total entries so far, and, if "signsplit" has been selected, the same stats again except split between positive and negative values.
The class can then have its 'updateStats' method called with a new number, which will recalculate all of the stats again with the new number included.
Importantly, the script does not store ANY data - it recalculates the stats using mathematical principals.

Thus, the class can calculate the stats for a data set of infinite size while using no memory space.

Example use:

a = variableStats(10) # initialise the object with '10' as the first input

a.sd # returns 0, as the standard deviation of one number is 0

a.mean # returns 10

\# Now we'll update it by running the value 20 through

a.updateStats(20) # Calculates the new stats without knowing all the numbers (does not store the initial '10')

a.sd # returns 5

a.mean # returns 15

a.sqrSum # returns 500, the sum of squares