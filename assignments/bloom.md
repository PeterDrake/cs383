# Overview
Hash tables are an extremely important data structure, but since we did the default version in class, a variation is needed for the project. This enjoyable project involves a very practical application related to cybersecurity. This is also another opportunity to read about and implement a new data structure.

**This is a team assignment. When you are done, *one* member of your team should submit the file, including (as a comment at the top of the file) the names of everyone who contributed.**

## The Task
A web browser maintains a list of known malicious domains so that it can warn users before they visit a site that might infect their computer with malware. New sites are being added to the list on a daily basis.

One simple approach would be to store all of the malicious domains in a hash table. That would make it simple to check if a given domain is on the list. The problem is that the list is too large: it would take up space on users' computers and require constantly pushing huge updates.

Google Chrome resolves this problem using a data structure called a Bloom filter. This structure is similar to a hash table, but uses far less space. Two prices are paid for this advantage:

The Bloom filter does not support deletion. This is not a problem in this application.
The Bloom filter is not entirely accurate. When asked if some domain is on the malicious list, it can't say "yes" or "no", but rather "maybe" or "no". In the extremely common case where the answer is "no", there's no need to do anything else. If the answer is "maybe", the browser remotely checks the master database on Google's servers. The point of the Bloom filter is to avoid this expensive check in most cases.

How does the Bloom filter work? [Read about it on Wikipedia.](https://en.wikipedia.org/wiki/Bloom_filter) (Don't worry about the Alternatives section.)

Your task is to implement a Bloom filter as a class `BloomFilter`, in a file `bloom.py`. It must provide methods `add`, `might_contain`, and (for testing purposes) `_true_bits`.

To run these, you will need two additional files, which should be in your project but not inside src. ***CONTENT WARNING: The names of some of these sites, especially on the bad list, may be deeply offensive. Such is the price of working with real-world data about the uglier part of the web. Let me know if this is a problem for you and we can arrange alternative data.***

bad.txt download  is a list of bad domains likely to contain malware. Whatever you do, don't go to any of these sites!
good.txt is a list of good domains.

# Files
* [test_bloom.py](../test/test_bloom.py)

You will need the two files below, which should be in your project but not inside src. ***CONTENT WARNING: The names of some of these sites, especially on the bad list, may be deeply offensive. Such is the price of working with real-world data about the uglier part of the web. Let me know if this is a problem for you and we can arrange alternative data.***

* [bad.txt](../bad.txt) download  is a list of [bad domains likely to contain malware](https://github.com/stamparm/blackbook/tree/master). <span style="color:red">***Whatever you do, don't go to any of these sites!***</span>
* [good.txt](../good.txt) is a list of [good domains](https://dataforseo.com/free-seo-stats/top-1000-websites).

# On Working as a Team

Take some time to talk about what worked on the last team project, what didn't, and how you might improve things. Do you have good processes for communication and passing files around? Is everyone contributing roughly equally? What technologies are helping or getting in the way?

Figure out how to break this assignment into steps and decide who is working on which part.

Be careful not to fall back on stereotypes when deciding who is going to do, for example, "coding" and "writing" work. Over the course of the semester, everyone on the team should get to do every kind of work.

# Hints
You're probably going to spend a lot more time thinking about this one than coding it. You're only writing four methods (including the constructor) and none of them are very long.

You should store your entire collection of bits in a single Python int, which is 0 for an empty filter.

You will use two hash functions. One uses the 16 low-order bits of the item's hash code, the other the 16 high-order bits. This means you'll need to do some bit-twiddling.

To get a 32-bit hashcode for some key, start with `abs(hash(key))`, then use `%` to make sure it's less than $2^{32}$.

There is an unrelated built-in Python called `filter`, so if you want to use that as a name in your program, use something else like `filter_`.

# Optional Challenge Problems
The "false positive" rate of this filter is still rather high (around 18%). Find a library that will allow you to get 64-bit hashcodes and then use the two 32-bit halves to index a larger bloom filter. The filter will therefore contain $2^{32} = 4294967296$ bits instead of $2^{16} = 65536$. Demonstrate empirically that this improves accuracy (at the expense of much more space).

If you've done that, compare various options such as using three 20-bit indices instead of two 32-bit indices. What seems to be a good tradeoff between accuracy and space?

# What to Hand in
Hand in your file `bloom.py` containing your `BloomFilter` class. Be sure to include the full names of everyone who worked on the project in a comment at the top of the file.