def swap_case(s):
    new_s = ""
    for c in s:
        if c.isupper():
            new_s += c.lower()
        else:
            new_s += c.upper()
    return new_s
