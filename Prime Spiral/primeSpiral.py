import matplotlib.pyplot as plt
import numpy as np

from functools import lru_cache
import typing
import math


@lru_cache(maxsize=None)
def get_primes(lower: int, upper: int) -> typing.Generator[int, None, None]:
    """Generate primes within the given range"""
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    break
            else:
                yield num


def get_coordinates(num: int) -> tuple:
    """Get the polar coordinates of a point"""
    return num * math.sin(num), num * math.cos(num)


def main():
    
    plt.style.use(['dark_background'])
    plt.figure(figsize=(40, 40))
    plt.axis("off")
    
    num = 1000000  # change the number of primes to get different results
    
    ar = [*map(get_coordinates, get_primes(0, num))]
    data = np.array(ar)
    x, y = data.T
    
    plt.scatter(x, y, s=2, c=np.random.rand(len(x), 3))
    plt.savefig(f"primes_{num}.png")
    plt.show()


if __name__ == "__main__":
    main()
