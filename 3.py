# -*- coding: cp1251 -*-


print("������� ������")
n = input()
s = ""
d = ""
for i in range(len(n)):
    if n[i] == "�":
        s = n[:i] + n[i + 1:]
        break

for i in range(len(s) - 1, 0, -1):
    if s[i] == "�":
        d = s[:i] + s[i + 1:]
        break

print(d)