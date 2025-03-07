class Solution(object):
    def isPrime(self, num):
        if num < 2:
            return False
        if num in (2, 3):
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def closestPrimes(self, left, right):
        primeNumber = []
        for num in range(left, right+1):
            self.isPrime(num) and primeNumber.append(num)
        if len(primeNumber) < 2:
            return [-1,-1]
        else:
            a = primeNumber[0]
            b = primeNumber[1]
            diff = [b-a,a,b]
            for i in range(2,len(primeNumber)):
                if diff[0] <= 2:
                    return [diff[1],diff[2]]
                a = b
                b = primeNumber[i]
                if b-a < diff[0]:
                    diff[0] = b-a
                    diff[1] = a
                    diff[2] = b
            return [diff[1],diff[2]]
        