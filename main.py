import sys, threading
# sys.setrecursionlimit(10**9) # max depth of recursion

from dfs_pn import run_dfs_pn
from dfs_bp import run_dfs_bp

tracks_size = [3]
print("Starting...")

for size in tracks_size:
    pn_traces, pn_states, pn_arcs = run_dfs_pn(size, 6*size)
    bp_traces, bp_states, bp_arcs = run_dfs_bp(size, 6*size)
    print("states bp:", bp_states)
    print("states pn:", pn_states)
    print("arcs bp:", bp_arcs)
    print("arcs pn:", pn_arcs)
    print("paths bp:", len(bp_traces))
    print("paths pn:", len(pn_traces))
    shared_paths = [x for x in bp_traces if x in pn_traces]
    print("shared paths:", len(shared_paths))
    only_bp = [x for x in bp_traces if x not in pn_traces]
    print("in bp not in pn:", len(only_bp))
    print(only_bp)
    only_pn = [x for x in pn_traces if x not in bp_traces]
    print("in pn not in bp:", len(only_pn))
    print(only_pn)
