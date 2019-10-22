# Fantasy Gold Teams website

Summary: this website calculates the best possible 4-man best ball fantasy golf teams for each given golf tournament based player birdie averages. In other words, it maximizes cumulative team birdie average while staying below team cost threshold.

# FAQ:
What is 4-man best ball fantasy golf? For each real golf tournament, you pick 4 players each round of the golf tournament. Those 4 players are you 4-man best ball team. You then get a score based on how well those 4 players scored in a best ball format.

What is best ball format? Take the best score amongst all team members on each hole, and that is the team score for that hole. Add up each team score on each hole and that's the team score for the round.


# Technical info:

Runtime comparisons:

|             | 77 players  | 129 players |
| ----------- | ----------- | ----------- |
| Python      | 1.09 sec    | 13.1 sec    |
| C++         | 0.10 sec    | 0.07 sec    |


Number of combinations of players:

140*139*138
---------------- = 447,580
     3*2*1

140*139
-------- = 9730
   2

Total: 447,580 + 9730 = 457,310
