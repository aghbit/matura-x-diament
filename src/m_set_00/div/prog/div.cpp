#include <iostream>

int main() {
    int n;
    std::cin >> n;

    int i = 2;
    while (i * i <= n) {
        if (n % i == 0) {
            std::cout << 1 << std::endl;
            return 0;
        }
        i++;
    }

    std::cout << 0 << std::endl;
    return 0;
}