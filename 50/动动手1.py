import math

class PrimeNum:
    def is_prime(self,number):
        if number > 1:
            if number == 2:
                return True
            if number % 2 == 0:
                return False
            for current in range(3, int(math.sqrt(number) + 1), 2):
                if number % current == 0:
                    return False
            return True
        return False
    
    def get_primes(self,number):
        while True:
            if self.is_prime(number):
                yield number
            number += 1
    
    def solve(self):
        total = 2
        for next_prime in self.get_primes(3):
            if next_prime < 2000000:
                total += next_prime
            else:
                print(total)
                return
 
if __name__ == '__main__':
    p = PrimeNum()
    p.solve()