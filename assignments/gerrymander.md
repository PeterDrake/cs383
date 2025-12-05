# Overview
This is a chance to apply your algorithm design skills to an important real-world problem for which there is no standard algorithm. It’s also an opportunity to write software that interacts with an existing framework.

**This is a team assignment. When you are done, *one* member of your team should submit the file, including (as a comment at the top of the file) the names of everyone who contributed.**

## The Task
[Gerrymandering](https://en.wikipedia.org/wiki/Gerrymandering) is drawing political district boundaries to favor one party or group. It can result in a considerable difference between the amount of support a party has and the portion of seats that party wins in the legislature -- even allowing the minority party to control the legislature. With the increasing availability of detailed data and geographic information systems, gerrymandering is becoming ever more sophisticated.

This assignment asks you to devise an algorithm to gerrymander a two-party electorate to favor a particular party. For simplicity, the voters are placed in a grid of hexagons. There will be d contiguous districts, each containing d voters.

You must create a class `Gerrymanderer` containing a method `gerrymander` that, given an `Electorate` (see the Files section below) and a party (a bool), returns a list of districts. Each district is a list of voters (which are integers in $[0, d^2)$ ) in that district.

## Ethical Note
Gerrymandering is antithetical to the central principle of electoral democracy: that every voter has equal power. This simulation is meant to explore the algorithmic issues related to gerrymandering and, tangentially, the surprisingly strong effect of gerrymandering. Computer scientists should not participate in actual efforts to corrupt the democratic process.

# Files
* [graph.py](../src/graph.py) is our simple undirected `Graph` class.
* [striper.py](../src/striper.py) is a simple implementation of the interface. It doesn't even look at the voters, but simply divides the electorate into either horizontal or vertical stripes depending on which party it is asked to gerrymander for.
* [electorate.py](../src/electorate.py) contains the `Electorate` class. An `Electorate` contains a `Graph` (indicating which voters are adjacent) and a list of votes. For example, if in `Electorate` `e` voter 12 favors the `True` party, `e.votes[12]` is `True`.
* [test_electorate.py](../test/test_electorate.py) contains unit tests for `electorate.py`. These tests already pass.
* [electorate_drawer.py](../src/electorate_drawer.py) graphically displays an electorate that has been divided into districts (showing only the edges that are within a district). Voters for the `True` party are shown as light yellow circles, those for the `False` party as dark purple. A paler hexagon behind each voter shows who won their district. Right now `electorate_drawer.py` uses an instance of `Striper` to do the gerrymandering, but you can edit the code at the bottom to use your class instead.
* [gerrymanderer_measurer.py](../src/gerrymanderer_measurer.py) measures the quality of a gerrymanderer. Again, it currently uses `Striper`, but is easily modified to use your class. Your goal is to maximize the output of this test. Since the voters' preferences are assigned randomly, you won't get exactly the same result from one run to the next, nor will it be possible to win every district. Still, **your class should outperform `Striper`**.

# Hints
Before you start, you may enjoy (and learn from) a [game](https://redslash12.itch.io/gerrymander) about gerrymandering that I helped make as part of a game jam a while back.

Except where specified above, do not modify any of the files given to you.

You have considerable room for creativity and ingenuity on this assignment. I don't have a specific solution in mind. In fact, to avoid the temptation to steer everyone toward the same answer, I have deliberately avoided writing a solution. Show me what you can do!

That said, don't hesitate to ask if you need ways to do various things as parts of your algorithm. A TA or I may be able to steer you toward an algorithm or even a library method that could save you hours of work.

Write unit tests! Your algorithm will almost certainly be divided into multiple methods. You need to be sure that each one does what you think it does.

I'm not asking you to formally analyze any algorithms involved, but analysis may be helpful in selecting algorithms for various parts of your solution. Brute force is not going to work here.

# Optional Challenge Problems
This assignment is challenging enough, but I may award a gold star for particularly clever, clear, efficient code and answers to the questions below.

# What to Hand in
Submit `gerrymanderer.py`, which contains your `Gerrymanderer` class. Be sure to include the full names of all of your team members in a comment at the top of the file.

 In a separate document, submit your answers to the following questions:

1. How does your algorithm work? Explain clearly, using diagrams if they help.
1. How effective is your algorithm on `Electorate`s of various sizes (9, 19, 29)?
1. What difficulties did you encounter and how did you overcome them?
1. How did your team work together to solve this problem? How can you improve this process in future projects?
