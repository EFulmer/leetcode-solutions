bool canBeValid(char* s, char* locked) {
    int N = strlen(s);
    if (N % 2 != 0) {
        return false;
    }

    int open_parens_count = 0;
    int available_unlocked_count = 0;

    int i = 0;
    for (i = 0; i < N; i++) {
        if (locked[i] == '0') {
            available_unlocked_count += 1;
        } else if (s[i] == '(') {
            open_parens_count += 1;
        } else if (s[i] == ')') {
            if (open_parens_count >= 1) {
                open_parens_count -= 1;
            } else if (available_unlocked_count >= 1) {
                available_unlocked_count -= 1;
            } else {
                return false;
            }
        }
    }

    int unpaired_opens_count = 0;
    for (i = N - 1; i >= 0; i--) {
        if (locked[i] == '0') {
            unpaired_opens_count -= 1;
            available_unlocked_count -= 1;
        } else if (s[i] == '(') {
            unpaired_opens_count += 1;
            open_parens_count -= 1;
        } else if (s[i] == ')') {
            unpaired_opens_count -= 1;
        }

        if (unpaired_opens_count > 0) {
            return false;
        }

        if ((available_unlocked_count == 0) && (unpaired_opens_count == 0)) {
            break;
        }
    }

    if (open_parens_count > 0) {
        return false;
    } else {
        return true;
    }
}
