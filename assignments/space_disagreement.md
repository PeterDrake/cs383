# Overview
This assignment asks you to implement a fairly complex graph algorithm that, like many others, comes down to depth-first search.

You are working for a computer game company producing a science fiction conquest game called *Space Disagreement!*. In this game, players move fleets between star systems connected by wormholes.

The AI team is in charge of the code that controls the alien enemies in the game. They need to identify strategic "choke points" where these tentacled abominations from the Widdershins Galaxy might build their fortresses. (In some versions of the [Risk game map](https://cf.geekdo-images.com/Pcf6sHxECBEbOv5NjuI5_g__imagepage/img/DD1brdg_kYNpj9UpkZ1r9ZhMBd0=/fit-in/900x600/filters:no_upscale():strip_icc()/pic96737.jpg), Indonesia is a choke point, cutting off Australia from the rest of the world.) They have called upon you, a renowned algorithms expert, to find such star systems in the game map. In graph theory terms, these are called *articulation points*.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

## The Task
In a file `articulation.py`, define a class `ArticulationPointFinder`. Once an instance is created (passing a graph into the initializer), the `is_articulation_point` attribute of the object should be a list of bools, indicating which vertices are articulation points.

You should use [Tarjan's algorithm](https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/) (not the naive approach described earlier on that page).

Because this is just depth-first search with some constant-time additions at each step, it runs in linear time.

# Files
* [test_articulation.py](../test/test_articulation.py)
* [graph.py](../src/graph.py)
* [space_disagreement.py](../src/space_disagreement.py)

# Hints
Yes, the page I linked you to on Tarjan's algorithm contains Python code. You are welcome to start with that code and adapt it so it works with my graph class and unit tests.

`space_disagreement.py` generates a graph, uses your class to find the articulation points, and displays the map graphically (with articulation points in a different color). If your initializer contains only the line

```python
self.is_articulation_point = [False] * len(graph.adj)
```

then you will be able to run this program and see a random map (without articulation points labeled).


# Optional Challenge Problems
Also find a list of *bridge edges*, which are edges that would make the graph disconnected if they were removed.

# What to Hand in
Hand in a single file `articulation.py`. It should contain your definition of `ArticulationPointFinder`.
