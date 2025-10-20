**Bring Levitin**

# Strassen's matrix multiplication (divide and conquer)
* Formula for 2x2 matrices from Levitin 189, but without the details of the constants (which each take one multiplication)
  * Uses 7 multiplications instead of 8
  * Not worth it for multiplying 2x2 matrices, but…
  * Subdivision, Levitin 190
  * Turns out to take time in only $n^{2.807}$
  * Other algorithms have got it down to $n^{2.376}$, but they are of only theoretical interest
* Who wins the bet on lower bound?
  * It must be at least $n^2$, because it takes that long to write down the answer
* If time, start implementing it
