# -*- coding: cp1251 -*-

n = input()
if n == n[::-1]:
    print(n, "- палиндром")
else:
    print(n, "- не палиндром")