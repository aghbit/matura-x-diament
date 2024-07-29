import random

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def make_test(n: int, path: str, prime: bool=False):
    n = random.randint(1, n)
    if prime:
        while not is_prime(n):
            n += 1
    with open(path, 'w') as f:
        f.write(f'{n}\n')

PATH = 'py_div'

DESC = {
    0: {
        'n': 10,
        'cnt': 2
    },
    1: {
        'n': 300,
        'cnt': 10
    },
    2: {
        'n': 10 ** 6,
        'cnt': 10
    },
    3: {
        'n': 10 ** 9,
        'cnt': 10
    }
}

if __name__ == '__main__':
    random.seed(42)
    for group, data in DESC.items():
        for i in range(data['cnt']):
            make_test(data['n'], f'in/{PATH}{group}{chr(ord("a") + i)}.in', prime=random.choice([True, False]))