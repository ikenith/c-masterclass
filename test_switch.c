#include <stdio.h>
int main() {
    int x = 1;
    switch (x) {
        x = x + 1; // Unreachable code before first case!
        case 1:
            printf("Choice is 1\n");
            break;
        case 2:
            printf("Choice is 2\n");
            break;
        default:
            printf("Default\n");
            break;
    }
    return 0;
}
