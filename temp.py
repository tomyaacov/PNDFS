import os
f = open(os.path.join("exports/","only_lc_bp_faults_R-1_L-16.csv"), "r")
runs = set([x.rstrip("\n") for x in f.readlines()])
new_runs = [x for x in runs if "A0,FE0,Le0" not in x]
with open("exports/only_" + "temp.csv", 'w') as f:
   f.write("\n".join(new_runs))