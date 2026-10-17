# 2026 World Cup Prediction Model

This project is a machine learning notebook for predicting the 2026 FIFA World Cup. It uses historical international match results, FIFA ranking data, and the group stage schedule to simulate the tournament and estimate each country's chance of winning.

## Data Files

#### `data/results.csv`

Historical international football results. This file is used to train the model. The notebook uses matches from 2010.

#### `data/FIFA_ranking.csv`

Information about the 48 teams in the 2026 World Cup. The FIFA rank and points are based on the official FIFA ranking update from 11 June 2026. The `host` column is equal to `1` for the host countries and `0` for all other teams.

#### `data/matches.csv`

The group stage match schedule used by the simulator. This file contains 72 matches: 12 groups with 6 matches in each group.

## Method

The notebook trains two Poisson regression models:

```text
model_home -> predicts goals scored by team1
model_away -> predicts goals scored by team2
```

The model uses simple features:

```text
FIFA rank of both teams
FIFA points of both teams
difference in rank
difference in FIFA points
host country indicator
neutral match indicator
```

After training, the notebook simulates matches by drawing goals from a Poisson distribution.

## Tournament Simulation

The notebook simulates:

```text
group stage
best third-placed teams
round of 32
round of 16
quarter-finals
semi-finals
final
```

For the group stage, teams are ranked by:

```text
points
goal difference
goals scored
FIFA ranking as a simple tie-breaker
```

## Output

The notebook produces:

```text
estimated title chances
predicted group standings
an example knockout bracket from one simulation
```

The Monte Carlo simulation is run 1000 times by default.


## Limitations

This is a deliberately simple model. It does not include:

```text
player injuries
travel distance
stadium effects
advanced Elo history
official third-place bracket mapping
penalty shootout strength
```

## Example Simulation Result

This is one example result from the notebook after running 1000 Monte Carlo simulations.

In knockout matches, if the simulated score is a draw, the winner is chosen randomly. This simplification is used because penalty shootouts are highly unpredictable.


### Highest Title Chances

| Place | Team | Chance |
|---:|---|---:|
| 1 | Argentina | 13.7% |
| 2 | France | 12.3% |
| 3 | Spain | 11.8% |
| 4 | England | 9.1% |
| 5 | Brazil | 6.3% |
| 6 | Morocco | 5.3% |
| 7 | Belgium | 4.5% |
| 8 | Netherlands | 4.3% |
| 9 | Portugal | 4.2% |
| 10 | Germany | 3.5% |

### Predicted Group Tables

| Group | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|
| A | Mexico | South Korea | Czech Republic | South Africa |
| B | Switzerland | Canada | Qatar | Bosnia and Herzegovina |
| C | Brazil | Morocco | Scotland | Haiti |
| D | United States | Turkey | Australia | Paraguay |
| E | Germany | Ecuador | Ivory Coast | Curacao |
| F | Netherlands | Japan | Sweden | Tunisia |
| G | Belgium | Iran | Egypt | New Zealand |
| H | Spain | Uruguay | Saudi Arabia | Cape Verde |
| I | France | Senegal | Norway | Iraq |
| J | Argentina | Austria | Algeria | Jordan |
| K | Portugal | Colombia | DR Congo | Uzbekistan |
| L | England | Croatia | Panama | Ghana |

### Example Knockout Bracket

#### Round of 32

| Team 1 | Score | Team 2 | Winner |
|---|---:|---|---|
| South Korea | 1 - 0 | Ghana | South Korea |
| Mexico | 1 - 1 | Colombia | Mexico |
| Switzerland | 4 - 0 | Scotland | Switzerland |
| Canada | 2 - 0 | Turkey | Canada |
| Brazil | 3 - 1 | Norway | Brazil |
| Morocco | 0 - 0 | South Africa | South Africa |
| United States | 2 - 1 | Qatar | United States |
| Australia | 1 - 1 | Algeria | Australia |
| Ecuador | 3 - 4 | Croatia | Croatia |
| Germany | 0 - 3 | England | England |
| Japan | 2 - 1 | Uzbekistan | Japan |
| Netherlands | 2 - 1 | Portugal | Netherlands |
| Belgium | 4 - 1 | Austria | Belgium |
| Iran | 1 - 3 | Argentina | Argentina |
| Spain | 1 - 0 | Senegal | Spain |
| Uruguay | 0 - 4 | France | France |

#### Round of 16

| Team 1 | Score | Team 2 | Winner |
|---|---:|---|---|
| South Korea | 1 - 3 | France | France |
| Mexico | 1 - 3 | Spain | Spain |
| Switzerland | 0 - 0 | Argentina | Switzerland |
| Canada | 0 - 2 | Belgium | Belgium |
| Brazil | 1 - 1 | Netherlands | Netherlands |
| South Africa | 0 - 4 | Japan | Japan |
| United States | 1 - 1 | England | United States |
| Australia | 2 - 2 | Croatia | Australia |

#### Quarter-finals

| Team 1 | Score | Team 2 | Winner |
|---|---:|---|---|
| France | 1 - 2 | Australia | Australia |
| Spain | 1 - 0 | United States | Spain |
| Switzerland | 1 - 1 | Japan | Japan |
| Belgium | 3 - 0 | Netherlands | Belgium |

#### Semi-finals

| Team 1 | Score | Team 2 | Winner |
|---|---:|---|---|
| Australia | 0 - 2 | Belgium | Belgium |
| Spain | 1 - 0 | Japan | Spain |

#### Final

| Team 1 | Score | Team 2 | Winner |
|---|---:|---|---|
| Belgium | 1 - 1 | Spain | Belgium |
