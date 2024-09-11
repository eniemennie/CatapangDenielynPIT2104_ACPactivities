set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

set1_difference = set1 - set2
print ("Set Difference of Set 1: ", set1_difference)
set2_difference = set2 - set1
print ("Set Diffference of Set 2: ", set2_difference)

set1_union = set1 | set2
print ("Union Set of Set 1: ", set1_union)
set2_union = set2 | set1
print ("Union Set of Set 2: ", set2_union)

set1_symdiff = set1 ^ set2
print ("Symmetric Difference of Set 1: ", set1_symdiff)
set2_symdiiff = set2 ^ set1
print ("Symmetric Difference of Set 2: ", set2_symdiiff)

set1_intersection = set1 & set2
print ("Intersection of Set 1: ", set1_intersection)
set2_intersection = set2 & set1
print ("Intersection of Set 2: ", set2_intersection)