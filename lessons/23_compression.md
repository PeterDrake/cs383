**Bring Sedgewick & Wayne**

# Compression
* Idea of compression
* ASCII: 8 bits per character (assuming extended ASCII, 7 otherwise)

## Morse code
* https://en.wikipedia.org/wiki/Morse_code#/media/File:International_Morse_Code.svg
* Note the need for pauses
  * In terms of bits, A is not really 01 but 10111000 (dot, space, dash, end of letter)
* TPS: What trend is there in which letters get which codes?

## Huffman codes
* Key idea: More common letters should get shorter codes, in order to shorten the message
* Example: ABRACADABRA!
  * 96 (= 12 * 8) bits with ASCII
  * If we use code in middle of S&W 826, only 17 bits, but you need spaces
* To avoid the need for spaces, no code should be a prefix of another
  * For code near bottom of S&W 826, 30 bits
* The code can be represented as a tree
  * Trees at upper right of S&W 827
    * Second one is better, only 29 bits for ABRACADABRA!
* How to find the best code?
  * Algorithm:
    * Create a forest of one-node trees, each with a character and its frequency
    * While there is more than one tree:
      * Merge the two lowest-frequency roots with a new root
      * How to find those roots? A priority queue!
  * Work through first couple of steps for ABRACADABRA!
  * TPS: Finish the tree
  * It can be proven (using induction) that this is an optimal code

## Discussion: Can you compress anything with this?
* What about something already compressed?
* Minimum description length (Kolmogorov complexity) cannot be computed!
