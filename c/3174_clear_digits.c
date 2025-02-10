#include <ctype.h>
#include <stdio.h>

char* clearDigits(char* s) {
    int n = strlen(s);
    char current_char;
    char * result;
    bool * indices_to_delete;
    int keep_count = 0;
    int i = 0;
    int j = 0;

    indices_to_delete = malloc(n * sizeof(int));
    if (indices_to_delete == NULL) {
        fprintf(stderr, "Memory allocation failed!");
        return NULL;
    }
    // Initialize indices_to_keep.
    for (i = 0; i < n; i++) {
        indices_to_delete[i] = false;
    }

    // Iterate through s:
    for (i = 1; i < n; i++) {
        current_char = s[i];
        if (isdigit(current_char)) {
            indices_to_delete[i] = true;
            j = i - 1;
            while (j >= 0) {
                if ( (!(isdigit(s[j]))) && (indices_to_delete[j] == false) ) {
                    indices_to_delete[j] = true;
                    break;
                } else {
                    j--;
                }
            }
        }
    }

    // Count how many indices to keep, for string allocation.
    for (i = 0; i < n; i++) {
        if (indices_to_delete[i] == false) {
            keep_count += 1;
        }
    }

    result = malloc((keep_count + 1) * sizeof(char));
    if (result == NULL) {
        fprintf(stderr, "Memory allocation failed!");
        return NULL;
    }

    j = 0;
    for (i = 0; i < n; i++) {
        if (indices_to_delete[i] == false) {
            result[j] = s[i];
            j++;
        }
    }
    result[j] = '\0';
    return result;
}
