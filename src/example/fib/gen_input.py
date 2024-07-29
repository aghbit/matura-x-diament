import random

def make_test(n: int, path: str):
    n = random.randint(1, n)
    with open(path, 'w') as f:
        f.write(f'{n} 1000000009\n')

PATH = 'fib'

DESC = {
    0: {
        'n': 10,
        'cnt': 3
    },
    1: {
        'n': 20,
        'cnt': 4
    },
    2: {
        'n': 100,
        'cnt': 10
    },
    3: {
        'n': 1000,
        'cnt': 20
    },
    4: {
        'n': 10 ** 6,
        'cnt': 20
    }
}

if __name__ == '__main__':
    random.seed(42)
    for group, data in DESC.items():
        for i in range(data['cnt']):
            make_test(data['n'], f'in/{PATH}{group}{chr(ord("a") + i)}.in')