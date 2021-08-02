from bp_graph import *


global_traces = []
visited = []
arcs = []

def dfs_bp(g, state, trace, depth):
    global global_traces, visited, arcs
    global_traces.append(trace)
    #if state not in visited:
    if depth > 0:
        visited.append(state)
        for key, value in g[state].items():
            arcs = arcs + [key]
            dfs_bp(g, value, trace + [key], depth - 1)


def run_dfs_bp(size, depth):
    global global_traces, visited, arcs
    global_traces = []
    visited = []
    arcs = []
    a = BPGraph("graphs/lc_bp_v1_" + str(size) + ".dot")
    dfs_bp(a.graph, a.start, [], depth)
    return global_traces, len(visited), len(arcs)