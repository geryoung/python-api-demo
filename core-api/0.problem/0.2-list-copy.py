#!/usr/bin/python# -*- coding utf-8 -*-

l1 = [1,2,3]
l2 = l1

l1[0] = 2

print l2


l3 = l1[:]
l1[0] = 3
print l3