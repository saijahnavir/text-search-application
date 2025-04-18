# boyer_moore.py

def boyer_moore_search(text, pattern):
    matches = []
    m = len(pattern)
    n = len(text)

    if m == 0 or n == 0 or m > n:
        return matches

    # Initialize bad character heuristic table
    bad_char = [-1] * 256
    for i in range(m):
        bad_char[ord(pattern[i])] = i

    s = 0  # shift of the pattern
    while s <= n - m:
        j = m - 1

        # Move from the end of the pattern towards the beginning
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # If a match is found
        if j < 0:
            matches.append(s)
            # Shift pattern based on bad character heuristic
            if s + m < n:
                s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
            else:
                s += 1
        else:
            # If no match is found, shift the pattern based on bad character heuristic
            # Ensure char_index is within valid bounds (0–255)
            char_index = ord(text[s + j]) if s + j < n else 0
            char_index = char_index % 256  # Ensure it's within 0–255
            s += max(1, j - bad_char[char_index])

    return matches
