# -*- coding: cp1251 -*-


print("введите строку")
n = input()
s = ""
d = ""
for i in range(len(n)):
    if n[i] == "о":
        s = n[:i] + n[i + 1:]
        break

for i in range(len(s) - 1, 0, -1):
    if s[i] == "л":
        d = s[:i] + s[i + 1:]
        break

print(d)