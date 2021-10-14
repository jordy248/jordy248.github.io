# -*- coding: utf-8 -*-

##### ---- #####
##### ---- #####
##### sets #####
##### ---- #####
##### ---- #####

### --------- ###
### resources ###
### --------- ###
'''
https://docs.python.org/3/tutorial/datastructures.html#sets
https://www.w3schools.com/python/python_ref_set.asp
'''

### ---------------- ###
### set construction ###
### ---------------- ###
set1 = set([1, 2, 3])
set2 = {1, 2, 3}
set3 = {element for element in [1, 2, 3]}

set1 == set2 == set3

### -------------- ###
### set operations ###
### -------------- ###

# ---------------------------------- #
# init sets A, B, C and 'universe' U #
# ---------------------------------- #
A = set([1, 2, 3,
         4, 5, 6])

B = set([4, 5, 6,
         7, 8, 9])

C = set([1, 2, 3,
         7, 8, 9])

U = set([i for i in range(100)])

# ----- #
# union #
# ----- #
A.union(B)

A | B

A.union(B) == A | B

# ------------ #
# intersection #
# ------------ #
A.intersection(B)

A & B

A.intersection(B) == A & B

A.isdisjoint(B)
A.isdisjoint(set(['not', 'in', 'A']))

# ------------------ #
# difference (minus) #
# ------------------ #
A.difference(B)

A - B

A.difference(B) == A - B

# -------------------------- #
# symmetric difference (XOR) #
# -------------------------- #
A.symmetric_difference(B)

A ^ B

A.symmetric_difference(B) == A ^ B

### ----------------- ###
### laws of operation ###
### ----------------- ###

# ---------- #
# complement #
# ---------- #
A__c = U.difference(A)

A.union(A__c) == U
A.intersection(A__c) == set()

A__c__c = U.difference(A__c)
A__c__c == A

# ----------- #
# commutative #
# ----------- #
A.union(B) == B.union(A)
A.intersection(B) == B.intersection(A)

# ---------- #
# demorgan's #
# ---------- #
A_u_B__c = U.difference(A).intersection(U.difference(B))
A_n_B__c = U.difference(A).union(U.difference(B))

# ----------- #
# associative #
# ----------- #
A.union(B.union(C)) == A.union(B).union(C)
A.intersection(B.intersection(C)) == A.intersection(B).intersection(C)

# ------------ #
# distributive #
# ------------ #
A.union(B.intersection(C)) == (A.union(B)).intersection(A.union(C))
A.intersection(B.union(C)) == (A.intersection(B)).union(A.intersection(C))
