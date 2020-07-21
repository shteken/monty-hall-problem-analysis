# Explanation

About the problem - https://en.wikipedia.org/wiki/Monty_Hall_problem
 
The file monty_hall_problem.py gets number of games and returns the success ratio of a participent who had chosen a door from the beginning of the game and didnt change his mind.

According to the statistics, this ratio is 1/3. Which means you want to change the door.
I wanted to test this number.

if you view the analysis.py code you will identify 2 main varibles - n and iter:
1. n - number of independent games the participent plays. Out of it, we can caluclate the success ratio - should be about 1/3. When n is bigger - the closer we get to 1/3.

2. iter - number of tests we conduct to get the distribution of the success ratio. Out of it, we have an object with length iter which each value is the success ratio of n independent games. When iter is bigger - the closer we get to success ratio of 1/3.

Run the file analysis.py to view for pairs of n and iter:
1. Histogram of the distribution
2. Cumulative distribution function of the distribution
3. Normal probability plot of the distribution
4. Analytical result - depends only on n (Mean, STD)
4. Estimated results (Mean, STD, Confidence Interval, Median)