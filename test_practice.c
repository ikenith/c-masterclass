#include <stdio.h>
#include <math.h>

int main(void) {
    // Q1: Sum of multiples of 3 or 5 below 1000
    int sum = 0;
    for (int i = 1; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }
    printf("Q1 Sum = %d\n", sum); // 233168

    // Q2: Roots of ax^2 + bx + c = 0
    double a = 1, b = -5, c = 6;
    double d = b*b - 4*a*c;
    if (d > 0) {
        double r1 = (-b + sqrt(d)) / (2*a);
        double r2 = (-b - sqrt(d)) / (2*a);
        printf("Q2 Roots: %.2f, %.2f\n", r1, r2);
    }

    // Q3: Largest among three
    int n1 = 15, n2 = 48, n3 = 32;
    int max = (n1 > n2) ? ((n1 > n3) ? n1 : n3) : ((n2 > n3) ? n2 : n3);
    printf("Q3 Largest = %d\n", max);

    // Q4: Even or Odd
    int num = 47;
    printf("Q4 %d is %s\n", num, (num % 2 == 0) ? "Even" : "Odd");

    // Q5: Remainder & Quotient
    int dividend = 29, divisor = 6;
    printf("Q5 Quotient = %d, Remainder = %d\n", dividend / divisor, dividend % divisor);

    // Q6: Even numbers between 100 and 200
    int count = 0;
    for (int i = 102; i < 200; i += 2) count++;
    printf("Q6 Even count strictly between 100 and 200 = %d\n", count);

    return 0;
}
