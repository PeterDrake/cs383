# Polynomial evaluation
* Class: implement obvious algorithm
* How many multiplications?
* Horner’s rule  
$ax^3 + bx^2 + cx + d$  
$= x(ax^2 +bx + c) + d$  
$= x(x(ax + b) + c) + d$  
$ = x(x(x(a) + b) + c) + d$  
* Implement
* How many multiplications?
# [Video on order notation](https://www.youtube.com/watch?v=w7-6h64HSQ8)
* Q&A
# Analyze orders of some algorithms we’ve seen
## fibo
* Brute force algorithm is in $\Theta(n)$
* Obvious recursive algorithm is in $\Theta(f(n)) = \Theta(\phi^n)$, where $\phi$ is roughly 1.618
* Closed form algorithm is in $\Theta(1)$
## gcd
* Brute force algorithm is in $O(\min(m, n)) = O(m + n)$
* Analysis of Euclid’s algorithm is more complicated, but it turns out to be in $O(\log(m + n))$
## log
* Algorithm by division (divide and conquer?) is in $\Theta(\log(n))$
* Faster algorithms exist, including table lookup
## exponent
* Brute force: $n - 1$ multiplications
* Divide and conquer: $log_{2}(n) + 1$ multiplications
## summations (e.g., sum of numbers from 1 through $n$)
* Brute force: $n - 1$ additions
* Closed form: constant time
## polynomial evaluation
* Brute force: quadratic
* Horner’s rule: linear 
## arithmetic ops
* Constant time *if you use a fixed size int*
* Picky theoreticians will talk about the number of bits required to represent the input, which for a number $n$ is $\log_{2}(n)$
