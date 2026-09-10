#include <stdio.h>
int a; // uninitialized global -> goes to .bss
int main() {
    printf("Hi");
    return 0;
}
