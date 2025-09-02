# What Makes a Program Fast?
* Which will be faster to sort 10000 random integers: C or Python?
* Vote
* [generate.py](../src/generate.py)
  * `python3 generate.py 10000 input.txt`
* [sort.c](../src/sort.c)
  * Both this and the Python version were written by ChatGPT
    * `gcc sort.c`
    * `./a.out input.txt`
    * `./a.out input.txt > cout`
  * [sort.py](../src/sort.py)
    * `python3 sort.py input.txt`
    * `python3 sort.py input.txt > pout`
  * So which one's faster?
    * `time ./a.out input.txt > cout`
    * `time python3 sort.py input.txt > pout`
  * Pretty close! Let's try 100000 numbers.
    * `python3 generate.py 100000 input.txt`
    * `time ./a.out input.txt > cout`
    * `time python3 sort.py input.txt > pout`

# History
[Slides](https://docs.google.com/presentation/d/1tY9IC_AFAy2aoJ9uvG2PZRleM5Suh_iFnrE-9l2fWgM/edit?usp=sharing)

# Test-Driven Development
* Euclid's algorithm
  * Finding gcd(a, b)
  * If b is 0, return a
  * Otherwise, find gcd(b, a % b)
  * How do we know that it will terminate?
  * How do we know that it will return the right answer?
* Unit test
* Code