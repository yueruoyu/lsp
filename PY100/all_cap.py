def all_cap(str):
    if len(str) > 10:
        return str.upper()
    else:
        return str

print(all_cap('hello world'))
print(all_cap('goodbye'))