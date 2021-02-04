def repeatedString(s, n):
    repeats = n//len(s)
    remain = n % len(s)
    return s.count('a')*repeats+s[:remain].count('a')


repeatedString('aba', 10)
