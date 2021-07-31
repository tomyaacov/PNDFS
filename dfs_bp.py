from bp_graph import *


global_traces = []
visited = []
arcs = []

def dfs_bp(g, state, trace):
    global global_traces, visited, arcs
    global_traces.append(trace)
    #print(trace)
    #g.goto(state)
    if state not in visited:
        visited.append(state)
        #l = list(g.successors())
        for key, value in g[state].items():
            arcs = arcs + [key]
            dfs_bp(g, value, trace + [key])


def run_dfs_bp(size):
    global global_traces, visited, arcs
    global_traces = []
    visited = []
    arcs = []
    a = BPGraph("graphs/lc_bp_v1_" + str(size) + ".dot")
    dfs_bp(a.graph, a.start, [])
    return global_traces, len(visited), len(arcs)