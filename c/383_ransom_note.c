bool canConstruct(char* ransomNote, char* magazine) {
    int* tally = malloc(26 * sizeof(int));
    int i;

    // Zero out the memory, just to be safe:
    for (i = 0; i < 26; i++) {
        tally[i] = 0;
    }
    // Populate the tally of characters found in the magazine:
    for (i = 0; i < strlen(magazine); i++) {
        tally[magazine[i] - 'a']++;
    }

    for (i = 0; i < strlen(ransomNote); i++) {
        if (tally[ransomNote[i] - 'a'] <= 0) {
            return false;
        }
        tally[ransomNote[i] - 'a']--;
    }
    return true;
}
