# Logarithms
* What do we know about logarithms?
  * Including "how many times do you have to divide"
  * Operations (increment -> exponent, decrement -> log)
  * Log bases
* Laws of logarithms
  * $a^b=c \Leftrightarrow\log_a c = b$
  * $\log_b a = \frac{\log_c a}{\log_c b}$
  * Stirling's approximation: $\log (n!) \in \Theta(n \log n)$
# Exponents
* $a^n = a \cdot a \cdot \ldots \cdot a$
* Class: write test and brute force implementation
* Divide and conquer approach for $a^n$ assuming $n$ is a positive integer
  * $1$ if $n = 0$
  * $(a^\frac{n}{2})^2$ if $n$ is even
  * $a \cdot (a^\frac{n-1}{2})^2$ if $n$ is odd
* Works because $(a^b)^c = a^{bc}$
* Class: implement it
* TPS: How many multiplications assuming $n$ is a power of 2?
  * $\log_2 n + 2$, because we divide $n$ in half at each step

# Plotting data
* See [plot_asymptotic.py](../src/plot_asymptotic.py)
* Plot $n^2$ from 1 to 100
* Add a second line for n

If time left, work on logarithms assignment
