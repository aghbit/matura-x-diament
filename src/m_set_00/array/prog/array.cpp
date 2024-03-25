#include <iostream>

long long array[1004];

int main() {
    int n, q;

    std::cin >> n >> q;

    for (int i = 0; i < n; i++) {
        std::cin >> array[i];
    }

    for (int i = 0; i < q; i++) {
        int idx;
        std::cin >> idx;
        std::cout << array[idx] << std::endl;
    }

    return 0;
}