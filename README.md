# Fantasy Gold Teams website

Summary: this website calculates the best possible 4-man best ball fantasy golf teams based on player birdie averages. The input you provide to the website are the list of available players to choose from, and the cost for each player. It assumes the allowable team budget is 30,000. The website will then maximize cumulative team birdie average while staying below team cost threshold.

#### FAQ:
What is 4-man best ball fantasy golf? For each real golf tournament, you pick 4 players each round of the golf tournament. Those 4 players are you 4-man best ball team. You then get a score based on how well those 4 players scored in a best ball format.

What is best ball format? Take the best score amongst all team members on each hole, and that is the team score for that hole. Add up each team score on each hole and that's the team score for the round.


#### Technical info:
Frontend: HTML/CSS/Jquery
Backend: Django + Cython (for the computationally expensive team calculation)

Cython was used given the number of calculations that need to be performed to guarantee the best teams are found. Below are some performance benchmarks from my own machine comparing the runtime of the team calculation in both python and c++.

Runtime comparisons:

|             | 77 players  | 129 players |
| ----------- | ----------- | ----------- |
| Python      | 1.09 sec    | 13.1 sec    |
| C++         | 0.10 sec    | 0.07 sec    |


Number of different combinations of players (assuming average of 140 players to choose from):

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{n!}{r!(n-r)!}&space;=&space;\frac{140!}{4!*136!}&space;=&space;\frac{140*139*138*137}{4*3*2*1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{n!}{r!(n-r)!}&space;=&space;\frac{140!}{4!*136!}&space;=&space;\frac{140*139*138*137}{4*3*2*1}" title="\frac{n!}{r!(n-r)!} = \frac{140!}{4!*136!} = \frac{140*139*138*137}{4*3*2*1}" /></a>

