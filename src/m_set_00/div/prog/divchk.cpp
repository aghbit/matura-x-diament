#include <cstring>
#include <fstream>
#include <iostream>

#include "oi.h"

int main(int argc, char ** argv) {
    int n;
    std::ifstream input(argv[1]);
    input >> n;

    bool is_prime;
    std::ifstream wzo(argv[2]);
    wzo >> is_prime;

    int odp;
    std::ifstream output(argv[3]);
    output >> odp;

    std::cerr << "n = " << n << ", is_prime = " << is_prime << ", odp = " << odp << std::endl;
    if (is_prime && odp != -1) {
        std::cerr << "Zły wynik" << std::endl;
        return 1;
    }
    if (odp <= 1 || odp >= n) {
        std::cerr << "Zwrócona liczba nie może być dzielnikiem zadanej liczby" << std::endl;
        return 1;
    }
    if (n % odp != 0) {
        std::cerr << "Zwrócona liczba nie jest dzielnikiem zadanej liczby" << std::endl;
        return 1;
    }

    std::cout << "Zwrócona liczba jest poprawna" << std::endl;
    return 0;
}