#!/usr/bin/python3

def isWinner(x, nums):
    # Implement the game logic here
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(num):
        primes = []
        for i in range(2, num + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def remove_multiples(arr, num):
        return [x for x in arr if x % num != 0]

    def can_win(primes, nums):
        for num in nums:
            if num not in primes:
                return True
            primes = remove_multiples(primes, num)
        return False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = get_primes(n)
        if can_win(primes, range(1, n + 1)):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

