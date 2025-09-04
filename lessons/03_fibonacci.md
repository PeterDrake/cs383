# Fibonacci Numbers
* Idea  
    $F(0) = 0$  
    $F(1) = 1$  
    $F(n) = F(n-1) + F(n-2)$  
* Naive recursive implementation
  * Create unit tests together
  * Have students implement it
  * Turns out to be really slow: $\Theta(F(n))$
  * Why: redundant computation
* Iterative array implementation
  * Have students implement it
  * Linear time
* Smarter recursive implementation
  * Provide implementation
  * Avoids redundant computation
  * Recursion is not inherently bad
  * Through clever tricks (and automatically in some languages), can be made to run in constant space
* Formula
  * $F(n) = \frac{\phi^n - (1-\phi)^n}{\sqrt{5}}$, where $\phi=\frac{1+\sqrt{5}}{2}$
  * Constant time and space!
  * Have students implement it
  * Why would this go badly for large $n$ in another language?
  * Who invented this? Wikipedia: "It has become known as Binet's formula, named after French mathematician Jacques Philippe Marie Binet, though it was already known by Abraham de Moivre and Daniel Bernoulli."
  * Stigler's Law of Eponymy: "No scientific discovery is named after its original discoverer"
    * Named after Stephen Stigler, invented by Robert Merton
