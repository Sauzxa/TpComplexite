#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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

    unsigned long long numbers[100];
    unsigned long long number;
    unsigned long long count = 0;
    srand((unsigned int)time(NULL));

    while (fscanf(input, "%llu", &number) == 1) {
        count++;
        if (count <= 100) numbers[count - 1] = number;
        else {
            unsigned long long index = (unsigned long long)rand() % count;
            if (index < 100) numbers[index] = number;
        }
    }
    fclose(input);

    if (count < 100) {
        printf("Input contains only %llu values; 100 are required\n", count);
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL) {
        printf("Cannot open output file %s\n", argv[2]);
        return 1;
    }
    for (int i = 0; i < 100; i++) fprintf(output, "%llu\n", numbers[i]);
    fclose(output);
    return 0;
}
