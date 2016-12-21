# DiceSumStats
## DiceSumStatistics or in other words, the number of ways to sum up to each number using a set of dice

This tool can be used to see how many ways you can combine dice together to sum up to a particular number.

## Usage
Code still needs some cleanup for the new DP solution.

## Concept
Consider the classic 2d6 problem. Imagine you have two six-sided fair dice. You roll the two dice and sum those numbers. How man times does each particular sum occur? In other words, how many ways can you combine two dice to sum up to 1, 2, 3, ..., max(d6) + max(d6)?
One could use a chart to show the combination of the first dice with the second dice.

For example,
```
\| 1| 2| 3| 4| 5| 6| <- what you roll on the first dice
--------------------
1| 2  3  4  5  6  7 <
2| 3  4  5  6  7  8 <
3| 4  5  6  7  8  9 <-their sum
4| 5  6  7  8  9 10 <
5| 6  7  8  9 10 11 <
6| 7  8  9 10 11 12 <
^-what you roll on the 2nd dice
```
And then you can manually see each sum, and then add up every occurence. Managable. 

But then what about a 3rd dice?

A 3D chart? I guess we can always use polynomial numbers/pascal's triangle or some obscure discrete formula that calculates multinomial coefficient (With n being number of dice in a roll, nd3 uses https://oeis.org/A027907 , nd4 uses https://oeis.org/A008287 , nd5 uses https://oeis.org/A035343 , nd6 uses https://oeis.org/A063260 etc.)

But then what about a 4th dice? That's not even a d6???

This is better off left to a computer to solve.
