# Trustpilot Challenge

This is my solution to the [challenge proposed by Trustpilot.](https://followthewhiterabbit.trustpilot.com/cs/step3.html)

I divided the problem into two different parts:
- **Filtering the wordlist according to the informationwe they give to us:** This is critical because obtaining a good subset will dramatically decrease the time needed to find the correct solution. I choose python to solve this part because it allows a fast developing and it's easy for playing with lists and strings.
- **Combine the wordlist, compute the md5 checksums and verify it:** I choose the C languaje for this part in order to obtain the lowest computation time (without using CUDA).

### Filter the wordlist
They give us the next anagram:
> poultry outwits ants

We basically do three steps in order to reduce the number of words:
- Remove the words that does not have the characters that they give to us on the anagram
- Remove the words that exceeds the number of characters they give to us on the anagram: For instance, if we know thta the maximum number of "o" is two, we remove all the words with three "o" on it.
- Remove the words that have characters that dont appear on the anagram.

### Combine the words and check it
