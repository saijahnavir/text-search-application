def rabin_karp_search(text, pattern, d=256, q=101):
    matches = []
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                matches.append(s)
        if s < n - m:
            t = (d*(t - ord(text[s])*h) + ord(text[s + m])) % q
            if t < 0:
                t += q
    return matches
