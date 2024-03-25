#include <fstream>
#include <iostream>

void endf(const char* msg, int line, int position) {
    std::cout << "WRONG" << std::endl;
    std::cout << "Line " << line << ": " << msg << std::endl;
    exit(0);
}

int main(int argc, char ** argv) {
    int n;
    std::ifstream input(argv[1]);
    input >> n;

    int odp;
    std::ifstream output(argv[2]);
    output >> odp;

    if (odp == -1) {
        for (int i = 2; i * i <= n; ++i) {
            if (n % i == 0) {
                std::cout << "WRONG" << std::endl;
                std::cout << "Dzielnik istnieje" << std::endl;
                return 0;
            }
        }
        std::cout << "OK" << std::endl;
        return 0;
    }
    if (odp <= 1 || odp >= n) {
        std::cout << "WRONG" << std::endl;
        std::cout << "Zwrócona liczba nie może być dzielnikiem" << std::endl;
        return 0;
    }
    if (n % odp != 0) {
        std::cout << "WRONG" << std::endl;
        std::cout << "Zwrócna liczba nie jest dzielnikiem" << std::endl;
        return 0;
    }

    std::cout << "OK" << std::endl;
    return 0;
}