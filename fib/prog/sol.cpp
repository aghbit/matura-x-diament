#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        std::cout << a << ' ';
        int c = a + b;
        a = b;
        b = c;
    }
    std::cout << '\n';
    return 0;
}