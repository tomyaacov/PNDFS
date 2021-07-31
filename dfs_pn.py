from level_crossing import get_net
from snakes.nets import *
import itertools


global_traces = []
visited = []
arcs = []


def dfs_pn(g, state, trace):
    global global_traces, visited, arcs
    global_traces.append(trace)
    #print(trace)
    g.goto(state)
    if state not in visited:
        visited.append(state)
        l = list(g.successors())
        arcs = arcs + l
        for s in l:
            dfs_pn(g, s[0], trace + [s[1].name])
    # else:
    #     l = list(g.successors())
    #     #print(len(l))
    #     for s in l:
    #         global_traces.append(trace + [s[1].name])
    # #print(g.completed())
    # if not g.completed():
    #     l = list(g.successors())
    #     #print(len(l))
    #     for s in l:
    #         dfs(g, s[0], trace + [s[1].name])
    # else:
    #     l = list(g.successors())
    #     #print(len(l))
    #     for s in l:
    #         global_traces.append(trace + [s[1].name])

def remove_helper_events(global_traces):
    helper_events = ['closingRequest', 'openningRequest', 'keepDown']
    global_traces = [list(filter(lambda a: a not in helper_events, x)) for x in global_traces]
    global_traces.sort()
    return list(k for k,_ in itertools.groupby(global_traces))
#visited.append(g.current())


def run_dfs_pn(size):
    global global_traces, visited, arcs
    global_traces = []
    visited = []
    arcs = []
    n = get_net(size)
    g = StateGraph(n)
    dfs_pn(g, g.current(), [])
    global_traces = remove_helper_events(global_traces)
    return global_traces, len(visited), len(arcs)

