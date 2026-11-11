# Romania A* Search

A* search on the classic Romania road map from *Artificial Intelligence: A Modern Approach* (Russell & Norvig). Given a starting city, it finds the shortest road route to Bucharest, using straight-line distance as the heuristic.

Originally written in 2019 for an Artificial Intelligence course at Institut Teknologi Sepuluh Nopember (ITS).

## Example

```bash
python astarRomania.py Arad
```

```
A* search on the Romania map
	Arad => Bucharest
=======================================================
Expanded cities		: Arad -> Sibiu -> Rimnicu Vilcea -> Fagaras -> Pitesti -> Bucharest
Number expanded		: 6
=======================================================
Shortest route		: Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
Cities on route		: 5
Total distance		: 418 km
```

Notice that A* expands Fagaras but doesn't take it: the Fagaras route reaches Bucharest in 450 km, while the route through Pitesti is 418 km. Greedy best-first search, which only looks at the heuristic, would take the longer Fagaras route.

## How it works

A* expands cities in order of **f(n) = g(n) + h(n)**:

- **g(n)**: road distance traveled from the start so far
- **h(n)**: straight-line distance from n to Bucharest

Straight-line distance never overestimates the real road distance, so the heuristic is **admissible** and A* is guaranteed to return the shortest route. The implementation uses a binary heap (`heapq`) as the priority queue and a closed set so each city is expanded at most once.

## Usage

Requires Python 3, with no extra packages.

```bash
python astarRomania.py            # from Arad (default)
python astarRomania.py Neamt      # from any city on the map
python astarRomania.py --help     # list all cities
```

The goal is always Bucharest, because the heuristic values in `romania_sld.txt` are distances to Bucharest.

## Data

| File | Format | Contents |
|---|---|---|
| [`romania.txt`](romania.txt) | `cityA,cityB,km` | 23 two-way roads between 20 cities |
| [`romania_sld.txt`](romania_sld.txt) | `city,km` | straight-line distance from each city to Bucharest |

## License

[MIT](LICENSE)
