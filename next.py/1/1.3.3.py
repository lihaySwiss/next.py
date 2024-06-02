def is_funny(string):
    return all(c in ('a', 'h') for c in string)

print(is_funny("haha"))
print(is_funny("helloaaaa"))
