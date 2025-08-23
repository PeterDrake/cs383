# Overview
This is another chance to apply your algorithm design skills to a complicated problem while interacting with existing software. You may well produce a program that can beat you!

**This is a team assignment. When you are done, *one* member of your team should submit the file, including (as a comment at the top of the file) the names of everyone who contributed.**

## The Task
Write an "artificially intelligent" opponent to play the game of [Scrabble](https://instructions.hasbro.com/api/download/04024_en-us_scrabble-board-game.pdf).

After downloading the files below, run `scrabble_gui.py` to play against a very weak opponent called `Incrementalist`. (You should have little trouble beating it, even if you are not a native English speaker.) It is important to play to refresh your knowledge of the rules and to become familiar with the somewhat unusual way in which moves are entered.

You can also run `tournament.py` to run a tournament between two instances of `Incrementalist`.

## Generative AI
*For this assignment only*, if you wish, you may make use of generative AI tools like ChatGPT, Gemini, or Copilot. Perhaps this will free you up to think about larger questions:
* How will we design this?
* How will we ensure that it is correct?
* How will we ensure that it is reasonably efficient?

You may not simply feed the entire assignment in as a prompt (and I suspect it is too long).

## Notes on the Word List

This word list may contain some surprising inclusions or omissions.

I got the list from Jeremy Gibson Bond, *Introduction to Game Design, Prototyping, and Development*, based on a list from Alan Beale, based on a list from Kevin Atkinson. 
I further modified it by:
* Switching it to lower case, and
* Prepending all of the legal two-letter and three-letter Scrabble words. 

The second change means that the words in the dictionary (a) are not in strictly alphabetical order and (b) may contain duplicates. Since the `Board` class manages the dictionary, you don’t have to worry about this.

Beale provides the following copyright notice:

> Alan Beale has released all of his word lists into the public domain apart from the aspects of the 2of12inf list that were based on the AGID word list, Copyright 2000 by Kevin Atkinson. Permission to use, copy, modify, distribute, and sell this [the AGID] database, the associated scripts, the output created from the scripts and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appears in all copies and that both that copyright notice and this permission notice appear in supporting documentation. Kevin Atkinson makes no representations about the suitability of this array for any purpose. It is provided "as is" without express or implied warranty.

# Files
The following should be **within a `scrabble` folder** inside your `src` folder:
* [words.txt](../src/scrabble/words.txt) is the word list.
* [location.py](../src/scrabble/location.py) contains the `Location` class, which represents either a square on the board or a direction. Notably, if `loc` is a `Location`, `loc + HORIZONTAL` is the square to the right of `loc`.
* [move.py](../src/scrabble/move.py) contains the classes `ExchangeTiles` and `PlayWord`. When your AI is asked for a move, it should return an instance of one of these classes.
* [gatekeeper.py](../src/scrabble/gatekeeper.py) contains the class `GateKeeper`, which serves as an interface between the board and your program.
* [incrementalist.py](../src/scrabble/incrementalist.py) contains the class `Incrementalist`, which is a very simple example AI. Like this one, yours should have methods `set_gatekeeper` and `choose_move`.
* [board.py](../src/scrabble/board.py) contains the elaborate `Board` class, which keeps track of the rules of the game.
* [tournament.py](../src/scrabble/tournament.py) allows two or more AI players to compete against each other.
* [scrabble_gui.py](../src/scrabble/scrabble_gui.py) allows a human player to play against an AI (with the AI moving first).

# Hints
Our version of the game only supports two players.

The regular "challenge" mechanism in Scrabble is replaced by a rule that nonwords are simply illegal to play.
		
Two reasonable strategies are to (a) find a good spot on the board, possibly one including a triple word score, and then find a word to put there, or (b) find a word from your hand and then try to place it on the board.

Your program need not find the very best move, but it should consistently trounce the `Incrementalist`.

You don't need to be clever about hand management (keeping a good balance of letters in your hand) or board position (not setting the opponent up to use valuable double and triple squares). Simply try to find a good, high-scoring word each turn.

Your code doesn't have to be lightning-fast, but if it's taking more than a few seconds per move it's too slow.

# Optional Challenge Problems
Have the best program in the tournament.

Find a bug in my code and report it. It's more useful if you can clearly describe how it happened, including a screenshot.

Create a GUI that allows you to watch two AIs play against each other. (`tournament.py` does show, in the console, the final board state and score after each game.)

Find a way to cheat! (You will be disqualified if your main program cheats, but you can submit a second one for this challenge.) The `GateKeeper` mechanism is meant to keep you from messing with the real Board, but there are ways around it. Can you describe a way to defend against your attack?

# What to Hand in
Submit the .py file for your class, given a creative name. Be sure to include the full names of all of your team members in a comment at the top of the class.

In a separate document, submit your answers to the following questions:

1. How does your algorithm work? Explain clearly, using diagrams if they help.
1. What is a typical final game score for your class?
1. What difficulties did you encounter and how did you overcome them?
1. How did your team work together to solve this problem? How can you improve this process in future projects?
