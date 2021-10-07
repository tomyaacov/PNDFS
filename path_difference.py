import os
import sys
import timeit

start = timeit.default_timer()

BP_FILE_NAME = sys.argv[1]#"lc_bp_R-1_L-16.csv"
PN_FILE_NAME = sys.argv[2]#"lc_pn_R-1_L-16.csv"

BP_file = open(os.path.join("exports/",BP_FILE_NAME), "r")
PN_file = open(os.path.join("exports/",PN_FILE_NAME), "r")

BP_runs = set([x.rstrip("\n") for x in BP_file.readlines()])
PN_runs = set([x.rstrip("\n") for x in PN_file.readlines()])

print("paths in BP:", len(BP_runs))
print("paths in PN:", len(PN_runs))

only_BP = BP_runs.difference(PN_runs)
print("only_BP:", len(only_BP))
only_PN = PN_runs.difference(BP_runs)
print("only_PN:", len(only_PN))
both = len(PN_runs) - len(only_PN)
print("both:", both)

with open("exports/only_" + BP_FILE_NAME, 'w') as f:
   f.write("\n".join(only_BP))

with open("exports/only_" + PN_FILE_NAME, 'w') as f:
   f.write("\n".join(only_PN)) 

stop = timeit.default_timer()

print('Time: ', stop - start) 