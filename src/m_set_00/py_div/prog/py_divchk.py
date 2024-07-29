import sys


def check(input_file, user_file, output_file):
    n = int(input_file.readline())
    user_output = int(user_file.readline())

    if user_output == -1:
        i = 2
        while i * i <= n:
            if n % i == 0:
                print("WRONG")
                print("Dzielnik istnieje")
                return
            i += 1
        print("OK")
        return
    elif user_output <= 1 or user_output >= n:
        print("WRONG")
        print("Zwrócona liczba nie może być dzielnikiem")
        return
    elif n % user_output != 0:
        print("WRONG")
        print("Zwrócona liczba nie jest dzielnikiem")
        return
    print("OK")
    return


if __name__ == "__main__":
    check(sys.stdin, open(sys.argv[1]), open(sys.argv[2]))
