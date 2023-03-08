This contains the solutions to the six programming assignments of the course Cryptography-I by Dan Boneh on Coursera.
Solutions to most of the assignments should be easily readable by code comments. 

In week1, the key is found by xoring the ciphertexts together. Note that on xoring with a space, the character just changes from upper-case to lower-case and vice versa. By doing this, we can eventually predict what one of the phrases mean and retrieve the key, following which we can decrypt the target ciphertext. Its more of an observation thing and hence not much insight is there in the code itself.

In week6, the challenge #3 is something that I want to particularly explain here. It is almost like challenge #1 with nuanced changes. First note that following similar steps of challenge #1, we can prove that `A^2 - 6N <= 1/(8*sqrt(6))`, where `A = (3p+2q)/2`. However, notice that A is not an integer, as p and q are primes and A is essntially `1.5p+q`. `1.5p` will not be an integer. So by doing `ceil(sqrt(6*N))` we obtain a number that is 0.5 more than A. 1.5 multiplied by any odd number will have a 0.5 left in its fractional part. So we subtract that 0.5 to fetch A. After that calculating x is straightforward. 

To calculate p and q, we had 4 choices. p = (A+x)/a and q = (A-x)/b such that ab = 6, so (a,b) = (1,6), (6,1), (2,3) and (3,2) were the choices. One of these gives integral prime values of p and q. Also notice that on printing it, we have some non-zero fractional part left in p and q. However, we can see that p = integer.0000000000000000000 ... 287359...

This easily tells us that the number is tending towards an integer, and the fractional part is due to lack of infinite precision which is impossible in square root operations. So mathematically, we are doing the right thing. Same is the case observed with q.
