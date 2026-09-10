#include <stdio.h>
int main() {
    printf("My mobile number is 8171243344\a\n");
    printf("Hello Geeks\b\bf\n");
    printf("Hello\tGFG\n");
    printf("Hello fri\rend\n");
    printf("a\\b\n");
    char* s = "A\072\065"; // \072 is octal 72 = 58 = ':', \065 is octal 65 = 53 = '5'
    printf("%s\n", s);
    char* y = "B\x4a";     // \x4a is hex 4A = 74 = 'J'
    printf("%s\n", y);
    return 0;
}
