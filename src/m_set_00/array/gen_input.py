import random

def make_test(n: int, q: int, max: int, path: str):
    n = random.randint(1, n)
    q = random.randint(1, q)
    with open(path, 'w') as f:
        f.write(f'{n} {q}\n')
        for _ in range(n):
           f.write(f'{random.randint(1, max)} ')
        f.write('\n')
        for _ in range(q):
            f.write(f'{random.randint(0, n - 1)}\n')

PATH = 'array'

DESC = {
    0: {
        'n': 10,
        'q': 6,
        'max': 10,
        'cnt': 3
    },
    1: {
        'n': 10,
        'q': 10,
        'max': 100,
        'cnt': 10
    },
    2: {
        'n': 100,
        'q': 100,
        'max': 10 ** 6,
        'cnt': 10
    },
    3: {
        'n': 1000,
        'q': 1000,
        'max': 10 ** 6,
        'cnt': 10
    },
    4: {
        'n': 1000,
        'q': 1000,
        'max': 10 ** 12,
        'cnt': 10
    }
}

if __name__ == '__main__':
    random.seed(42)
    for group, data in DESC.items():
        for i in range(data['cnt']):
            make_test(data['n'], data['q'], data['max'], f'in/{PATH}{group}{chr(ord("a") + i)}.in')