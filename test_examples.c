#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int global_a; // in BSS
int global_b = 42; // in Data

int main(void) {
    // 1. Hello World
    printf("Hello, World!\n");

    // 2. Precedence / Relational chaining
    int a = 1, b = 2, c = 3;
    int d = a > b < c; // (1 > 2) is 0, 0 < 3 is 1
    printf("d = %d\n", d);

    // 3. Bitwise complement
    int val = 35;
    printf("~35 = %d\n", ~val); // -36

    // 4. Ternary biggest of 3
    int x = 15, y = 42, z = 27;
    int big = x > y ? (x > z ? x : z) : (y > z ? y : z);
    printf("big = %d\n", big);

    // 5. printf return value
    int ret_printf = printf("geeksforgeeks");
    printf(" %d\n", ret_printf);

    // 6. Short-circuiting
    int sc_a = 10, sc_b = 4;
    bool res1 = ((sc_a == sc_b) && printf("C Language\n")); // should not print
    printf("res1 = %d\n", res1);
    bool res2 = ((sc_a != sc_b) || printf("C Language\n")); // should not print
    printf("res2 = %d\n", res2);

    // 7. Sum of digits
    int n = 1234, sum = 0;
    while (n != 0) {
        sum += n % 10;
        n /= 10;
    }
    printf("sum of digits = %d\n", sum);

    return 0;
}
