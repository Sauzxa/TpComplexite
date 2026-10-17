#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int count_digits(unsigned long long number) {
    int count = 1;
    while (number >= 10) {
        number /= 10;
        count++;
    }
    return count;
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

    unsigned long long numbers[7][10];
    unsigned long long counts[7] = {0};
    unsigned long long number;
    srand((unsigned int)time(NULL));

    while (fscanf(input, "%llu", &number) == 1) {
        int digits = count_digits(number);
        if (digits >= 3 && digits <= 9) {
            int group = digits - 3;
            counts[group]++;
            if (counts[group] <= 10) numbers[group][counts[group] - 1] = number;
            else {
                unsigned long long index = (unsigned long long)rand() % counts[group];
                if (index < 10) numbers[group][index] = number;
            }
        }
    }
    fclose(input);

    for (int group = 0; group < 7; group++) {
        if (counts[group] < 10) {
            printf("Input has only %llu values with %d digits; 10 are required\n",
                   counts[group], group + 3);
            return 1;
        }
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL) {
        printf("Cannot open output file %s\n", argv[2]);
        return 1;
    }
    for (int group = 0; group < 7; group++) {
        for (int i = 0; i < 10; i++) fprintf(output, "%llu\n", numbers[group][i]);
    }
    fclose(output);
    return 0;
}
