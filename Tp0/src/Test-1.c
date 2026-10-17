#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int is_prime(unsigned long long number) {
    if (number < 2) return 0;
    if (number == 2) return 1;
    if (number % 2 == 0) return 0;
    for (unsigned long long i = 3; i <= number / i; i += 2) {
        if (number % i == 0) return 0;
    }
    return 1;
}

int main(int argc, char **argv) {
    if (argc != 3) {
        printf("Usage: %s <input-file> <output-file>\n", argv[0]);
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL) {
        printf("Cannot open input file %s\n", argv[1]);
        return 1;
    }

    unsigned long long primes[100];
    unsigned long long number;
    unsigned long long count = 0;
    srand((unsigned int)time(NULL));

    while (fscanf(input, "%llu", &number) == 1) {
        if (number >= 1000 && number <= 1000000 && is_prime(number)) {
            count++;
            if (count <= 100) primes[count - 1] = number;
            else {
                unsigned long long index = (unsigned long long)rand() % count;
                if (index < 100) primes[index] = number;
            }
        }
    }
    fclose(input);

    if (count < 100) {
        printf("Input contains only %llu eligible primes; 100 are required\n", count);
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL) {
        printf("Cannot open output file %s\n", argv[2]);
        return 1;
    }
    for (int i = 0; i < 100; i++) fprintf(output, "%llu\n", primes[i]);
    fclose(output);
    return 0;
}
