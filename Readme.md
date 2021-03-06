# Trustpilot Challenge

This is my solution to the [challenge proposed by Trustpilot.](https://followthewhiterabbit.trustpilot.com/cs/step3.html)

I divided the problem into two different parts:
- **Filtering the wordlist according to the information they give to us:** This is critical because obtaining a good subset will dramatically decrease the time needed to find the correct solution. I choose python to solve this part because it allows a fast developing and it's easy for playing with lists and strings.
- **Combine the wordlist, compute the md5 checksums and verify it:** I choose the C language for this part in order to obtain the lowest computation time (without using CUDA).

### Filter the wordlist
They give us the next anagram:
> poultry outwits ants

We basically do three steps in order to reduce the number of words:
- Remove the words that does not have the characters that they give to us on the anagram
- Remove the words that exceeds the number of characters they give to us on the anagram: For instance, if we know that the maximum number of "o" is two, we remove all the words with three "o" on it.
- Remove the words that have characters that don't appear on the anagram.

### Combine the words and check it

Now that we have the reduced dictionary we need to make all the combinations possible with three elements (I assumed it's a three word sentence because there are two spaces), compute its md5 hash and check if some of these hashes coincide with the ones trustpilot gave to us:

> The MD5 hash of the easiest secret phrase is "e4820b45d2277f3844eac66c903e84be"

> The MD5 hash of the more difficult secret phrase is "23170acc097c24edb98fc5488ab033fe"

> The MD5 hash of the hard secret phrase is "665e5bcb0c20062fe8abaaf4628bb154"

This part is very straight forward. The only interesting thing here it's that we used pthreads to parallelize the checking part. In fact, there are some improvements that could have been implemented:
- ~~Check if three word sentence exceeds the length of the anagram. In that case the sentence could be discarded without computing and checking the md5 hash.~~
- Check if some of the characters of the whole sentence exceeds the number of appearances, just like I did on the filtering phase, but with the whole sentence.

I did some benchmarks (nothing too scientific) using four cores of an i7-3770 @ 3.40GHz. It did 400.000 comparisons in 2 seconds. That is 50.000 md5's/sec per core. This is fast or slow? Well, Openssl (`openssl speed md5`) did roughly 4 millions md5's/sec on the same machine so I think there is room for improvements, although I suspect openssl uses some sort of ultra low level Tntel tricks and speciallized hardware to speed up the hashing.

### Results

With this code and a pretty powerful multicore computer I was able to obtain the medium and the easiest hash. The hardest though, escaped from my algorithm.

### Where is the third hash

I've some ideas about where to find the third hash:

- We assume the solution had three words. That's true for the two first hashes but the third one could be hidden behind a two words sentence or a four words sentence

### Using hashcat

Instead of using my little program we could use [hashcat](https://hashcat.net/hashcat/). Hashcat is a password recovery tool which perform bruteforcing similar to the code I wrote, but it has some advantages like the use of GPU for fastest hash calculation.

```
echo e4820b45d2277f3844eac66c903e84be > hashes.txt
echo 23170acc097c24edb98fc5488ab033fe >> hashes.txt
echo 665e5bcb0c20062fe8abaaf4628bb154 >> hashes.txt
hashcat -m 0 -a 0 hashes.txt (and something more here)
```
