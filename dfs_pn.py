from level_crossing import get_net
from snakes.nets import *
import itertools
from bp_graph import *


global_traces = []
visited = []
arcs = []


def dfs_pn(g, state, trace, depth):
    global global_traces, visited, arcs
    global_traces.append(trace)
    g.goto(state)
    #if state not in visited:
    if depth > 0:
        l = list(g.successors())
        if state not in visited:
            visited.append(state)
            arcs = arcs + l
        for s in l:
            if s[1].name in ['closingRequest', 'openningRequest', 'keepDown']:
                dfs_pn(g, s[0], trace + [s[1].name], depth)
            else:
                #print(s[1].name)
                dfs_pn(g, s[0], trace + [s[1].name], depth - 1)


def remove_helper_events(global_traces):
    helper_events = ['closingRequest', 'openningRequest', 'keepDown']
    global_traces = [list(filter(lambda a: a not in helper_events, x)) for x in global_traces]
    global_traces.sort()
    return list(k for k,_ in itertools.groupby(global_traces))
#visited.append(g.current())


def run_dfs_pn(size, depth):
    global global_traces, visited, arcs
    global_traces = []
    visited = []
    arcs = []
    n = get_net(size)
    g = StateGraph(n)
    dfs_pn(g, g.current(), [], depth)
    global_traces = remove_helper_events(global_traces)
    return global_traces, len(visited), len(arcs)

#print(run_dfs_pn(2))

# def dfs_pn(g, state, trace, depth):
#     global global_traces, visited, arcs
#     global_traces.append(trace)
#     #if state not in visited:
#     if depth > 0:
#         visited.append(state)
#         for key, value in g[state].items():
#             arcs = arcs + [key]
#             dfs_pn(g, value, trace + [key], depth - 1)


# def remove_helper_events(g):
#     done = False
#     while not done:
#         done = remove_helper_events_single(g.graph)


# def remove_helper_events_single(g):
#     for source, d in g.items():
#         for event, destination in d.items():
#             if event in ['ClosingRequest', 'OpeningRequest', 'KeepDown']:
#                 g[source].pop(event)
#                 g[source].update(g[destination])
#                 return False
#     return True


# def run_dfs_pn(size, depth):
#     global global_traces, visited, arcs
#     global_traces = []
#     visited = []
#     arcs = []
#     a = BPGraph("graphs/lc_pn_check_" + str(size) + ".dot")
#     remove_helper_events(a)
#     # print(a.graph)
#     # print(a.start)
#     dfs_pn(a.graph, a.start, [], depth)
#     return global_traces, len(visited), len(arcs)