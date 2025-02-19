int percentageLetter(char* s, char letter) {
    double count = 0;
    for (int i = 0; i < strlen(s); i++) {
        count = count + (s[i] == letter);
    }
    return (int)((count / strlen(s)) * 100);
}
