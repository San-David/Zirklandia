# Zirklandia
A recreation of an activity in my Geography class. Uses Python 3.6

HOW IT WORKS

Zirklandia

* Continent filled with independent states.
* In first iteration, the continent will be a square grid of a certain size. I’ll work out how to make a randomly generated continent when I get better at coding.

Choosing a state

* States can be chosen either individually by each player, or randomly assigned to each player.
* If players opt to choose individually…
* Each player is given a random number. The lowest number picks their state first.
* Players could just be assigned to a state randomly.
* Each player is given a random number that corresponds to a state.


Attacking, defending, and deterring with resources.

* Attacking and defending are used in the Action Phase.
* States that deter "x" amount will get that "x" amount of resources permanently, at the beginning of the next round.
  * State 1 starts with 16 resources.
  * State 1 will deter 8 resources on R1.
  * State 1 will have 24 resources on R2.
  * State 1 will deter 12 resources on R2.
  * State 1 will have 36 resources on R3.
  * State 1 will deter 0 resources on R3.
  * State 1 will have 36 resources on R4.
* Could allow players to choose the amount of resources that they start with.

Discovery

* May not implement this in first iteration.
* States discover other states, depending on the round.
  * First fourth of game: Adjacent states
  * Second fourth of game: Adjacent states + connected by rivers
  * Third fourth of game: Adjacent states + connected by rivers and sea
  * Last fourth of game: All states
* Once another state has been discovered, it cannot be undiscovered.
* Discovery could be changed to be based on the technology a state has, but I’d have to create some complicated system that I don’t want to deal with at the moment.

Deliberation Phase

* One minute at the start of the game, adds one minute per round to a maximum of five minutes.
  * R1: 1 min
  * R2: 2 min
  * R3: 3 min
  * R4: 4 min
  * R5: 5 min
  * R6: 5 min, etc
* Could also allow players to choose the amount of time allotted, and the rate that the time allocation increases.
* States can determine what resources they want to use for offense, defense, and deterrence.
* States can choose to end their Deliberation Phase at any point. If all states end their Deliberation Phase before time's up, the game will automatically progress to the Action Phase.
* Once the Deliberation Phase ends, states cannot change what resources they have allocated.

Action Phase

* In a random order, states reveal their offense allocation and the state they want to subsume.
* States can only attack states that they have discovered.
* States will determine the state that they want to subsume at the beginning of their turn during the Action Phase.
* Defense allocation is only revealed if they are attacked.
* Deterrence allocation is never revealed.
* Total resources is never revealed until the end of the game.

Battle

* Countries will get a random number from 1 to (insert number here, probably 3) for each resource point that they use. The state with the higher total score will win the battle.
  * Example code: https://repl.it/EdFE/7 
* If the attacker wins, then the attacker will subsume the defender, gaining half of the defender's total resources, and the defender will be eliminated.
* If the defender wins, then the attacker will lose a quarter of their resources.
* If the total amount of resources left has a fraction of a resource, then the fraction is lost (round the number down).
* State 1 attacks, and loses 4.5 out of their 18 resources, leaving them at 13.5. Because there is a fraction of a resource, the total amount goes down to 13.
* Terrain bonuses
  * Mountains, provide percent bonus to defense (1.25x?)
  * Fertile Plains, provide bonus to deterrence (1.25x?)
  * Rivers (or some other type of terrain, need ideas), provide bonus to offense (1.25x?)
* Should be a percent bonus, rather than a flat bonus. As seen in the game we played, a bonus of 1 to defense hardly mattered when states had values of 200 for defense. By making it a percent bonus, then, instead it being 200 -> 201, it’s, say, 200 -> 250, for a 1.25x bonus.



Alliances

* States can choose to come to another state's aid, whether it is for offense or defense, provided that they have discovered each other.
* Can only decided during the Deliberation Phase.
* When allied, each state’s total resources will be shown to each member of the alliance. Resources will be decided individually between each state.
* If an alliance attacks, the total resources allocated to offense among all states in the alliance will be used.
* If S1 and S2 are in an alliance, and S1 allocates 4 to offense, while S2 allocated 6 to offense, then they will use 10 as their value for offense.
* If a member of an alliance is attacked, then the total resources allocated to defense among all states will be used.
* If S1 and S2 are in an alliance, and S1 allocates 8 to defense, while S2 allocates 2 to defense, then they will use 10 as their value for defense.
* States can easily leave an alliance.

Winning the Game

* The primary goal is to take over the largest amount of sq. miles / km. of land.
* However, other goals could include amassing the largest amount of resources, surviving the longest, etc.
