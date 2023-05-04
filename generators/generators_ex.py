# %% Tasks
'''
1) Write a generator function that generates the first n squares of integers, starting from 0. For example, if n=5, the generator should produce the sequence 0, 1, 4, 9, 16.

2) Write a generator function that takes a list of integers as input, and yields the sum of the previous two integers in the list for each value in the list. For example, if the input list is [1, 2, 3, 4], the generator should produce the sequence 3, 5, 7.

3) Write a generator function that takes a string as input, and yields each word in the string in reverse order. For example, if the input string is "hello world", the generator should produce the sequence "olleh", "dlrow".

4) Write a generator function that generates all the prime numbers less than or equal to a given integer n. For example, if n=10, the generator should produce the sequence 2, 3, 5, 7.

5) Write a generator expression that generates a sequence of tuples (i, j) for all integers i and j such that i < j and i is even and j is odd. For example, the generator should produce the sequence (0, 1), (0, 3), (2, 3), (2, 5), (4, 5), (4, 7), ....

6) Write a generator that produces the fibonacci sequence in a lazy manner.

7) Write a generator function that takes a list of stock prices and yields the percentage change between each pair of consecutive prices. For example, if the input list is [10, 12, 8, 15, 11], the generator should produce the sequence 0.2, -0.333, 0.875, -0.267.

8) Write a generator function that generates the moving average of a list of stock prices for a given window size k. For example, if the input list is [10, 12, 8, 15, 11] and k=3, the generator should produce the sequence 10.0, 10.666, 11.666, 11.333.

9) Write a generator function that generates the cumulative return of a list of stock prices over time. For example, if the input list is [10, 12, 8, 15, 11], the generator should produce the sequence 0.0, 0.2, -0.2, 0.5, 0.1.

10) Write a generator function that takes a list of stock prices and yields the top k largest percentage price gains for any n-day period, where n is a parameter of the function. For example, if the input list is [10, 12, 8, 15, 11, 20, 18, 22] and n=3 and k=2, the generator should produce the sequence 0.667, 1.75, which represents the top two largest percentage gains for any 3-day period in the list ((8, 15, 11) and (11, 20, 18)).

11) Write a generator function that takes a list of playing cards and yields only the face cards (Jacks, Queens, and Kings) in the list. For example, if the input list is ["Ace", "Jack", "3", "Queen", "King", "10"], the generator should produce the sequence "Jack", "Queen", "King".

12) Write a generator function that generates all possible combinations of cards in a standard deck of playing cards, without repetition. For example, the generator should produce the sequence ("Ace", "Spades"), ("2", "Spades"), ..., ("King", "Diamonds").

13) Write a generator function that takes a list of playing cards and yields all possible pairs of cards in the list, without repetition. For example, if the input list is ["Ace", "Jack", "3", "Queen"], the generator should produce the sequence ("Ace", "Jack"), ("Ace", "3"), ("Ace", "Queen"), ("Jack", "3"), ("Jack", "Queen"), ("3", "Queen").

14) Write a generator function that generates all possible hands of a given size k from a list of playing cards, without repetition. For example, if the input list is ["Ace", "Jack", "3", "Queen", "King"] and k=2, the generator should produce the sequence ("Ace", "Jack"), ("Ace", "3"), ..., ("King", "Queen").

15) Write a generator function that connects to a web server and yields the HTML content of each page on the site, following links recursively to traverse the entire site.
'''
# %% ad1)
def squares(nums):
    for i in nums:
        yield i**2

# example usage
for s in squares(range(5)):
    print(s)
# %% ad2)
def prev_sum(lst):
    it = iter(lst)
    a = next(it, 0)
    b = next(it, 0)
    yield a + b
    for c in it:
        a, b = b, c
        yield a + b

# example usage
for s in prev_sum([1, 2, 3, 4]):
    print(s)
# %% ad3)
def reverse_words(s):
    for word in s.split():
        yield word[::-1]

# example usage
for w in reverse_words("hello world"):
    print(w)
# %% ad4)
def primes(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    for i in range(n+1):
        if sieve[i]:
            yield i

# example usage
for p in primes(10):
    print(p)
# %% ad5)
pairs = ((i, j) for i in range(0, 10, 2) for j in range(1, 10, 2) if i < j)

# example usage
for p in pairs:
    print(p)
# %% ad6)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for fib in fibonacci(10):
    print(fib)
# %% ad7)
def price_change(prices):
    it = iter(prices)
    a = next(it, 0)
    for b in it:
        yield (b-a)/a
        a = b

# example usage
for p in price_change([10, 12, 8, 15, 11]):
    print(p)
# %% ad8)
def moving_average(prices, k):
    it = iter(prices)
    q = [next(it, 0) for i in range(k)]
    s = sum(q)
    yield s / k
    for p in it:
        s += p - q.pop(0)
        q.append(p)
        yield s / k

# example usage
for ma in moving_average([10, 12, 8, 15, 11], 3):
    print(ma)
# %% ad9)
def cumulative_return(prices):
    it = iter(prices)
    a = next(it, None)
    yield 0
    for b in it:
        yield (b-a)/a
        a = b

# example usage
for cr in cumulative_return([10, 12, 8, 15, 11]):
    print(cr)
# %% ad10)
def top_gains(prices, n, k):
    gains = []
    for i in range(len(prices) - n+1):
        change = (prices[i+n-1] - prices[i]) / prices[i]
        gains.append(change)
    for gain in sorted(gains, reverse=True)[0:k]:
        yield round(gain, 3)

# example usage
for tg in top_gains([10, 12, 8, 15, 11, 20, 18, 22], 3, 2):
    print(tg)
# output: 0.636, 0.375
# %% ad11)
def face_cards(cards):
    for card in cards:
        if card in ("Jack", "Queen", "King"):
            yield card

# example usage
for fc in face_cards(["Ace", "Jack", "3", "Queen", "King", "10"]):
    print(fc)
# %% ad12)
def card_combinations():
    ranks = ["Ace"] + [str(i) for i in range(2, 11)] + ["Jack", "Queen", "King"]
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    for rank in ranks:
        for suit in suits:
            yield (rank, suit)

# example usage
for cc in card_combinations():
    print(cc)
# %% ad13)
def card_pairs(cards):
    it1 = iter(cards)
    for card1 in it1:
        it2 = iter(cards)
        for card2 in it2:
            if card1 != card2:
                yield (card1, card2)

# example usage
for cp in card_pairs(["Ace", "Jack", "3", "Queen"]):
    print(cp)
# %% ad14)
from itertools import combinations

def card_hands(cards, k):
    for hand in combinations(cards, k):
        yield hand

# example usage
for ch in card_hands(["Ace", "Jack", "3", "Queen", "King"], 2):
    print(ch)
# %% ad15)
import requests
from bs4 import BeautifulSoup

def crawl_website(url, visited=None):
    if visited is None:
        visited = set()
    if url in visited:
        return
    visited.add(url)
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    yield soup.prettify()
    for link in soup.find_all('a'):
        next_url = link.get('href')
        if next_url is not None and next_url.startswith('http'):
            yield from crawl_website(next_url, visited)

# example usage
page = crawl_website('https://www.realtotal.de/')
next(page)
# %%
