bool canConstruct(char* s, int k) {
    int i = 0;
    int N = strlen(s);

    if (N == k) {
        return true;
    } else if (k > N) {
        return false;
    }

    int counter[26];
    char current_letter;
    for (i = 0; i < N; i++) {
        current_letter = s[i] - 'a';
        counter[current_letter] += 1;
    }
    int odd_character_count = 0;
    for (i = 0; i < 26; i++) {
        if ((counter[i] % 2) != 0) {
            odd_character_count += 1;
        }
        if (odd_character_count > k) {
            return false;
        }
    }
    if (odd_character_count > k) {
        return false;
    } else {
        return true;
    }
}
