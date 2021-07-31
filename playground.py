# from level_crossing import get_net
# from snakes.nets import *
# import itertools
# global_traces = []
# visited = []
# n = get_net(1)#'approaching0', 'entering0', 'approaching0'
# n.transition('approaching0').fire(n.transition('approaching0').modes()[0])
# n.transition('closingRequest').fire(n.transition('closingRequest').modes()[0])
# n.transition('lower').fire(n.transition('lower').modes()[0])
# n.transition('entering0').fire(n.transition('entering0').modes()[0])
# n.transition('leaving0').fire(n.transition('leaving0').modes()[0])
# n.transition('openningRequest').fire(n.transition('openningRequest').modes()[0])
# n.transition('approaching0').fire(n.transition('approaching0').modes()[0])
# n.transition('closingRequest').fire(n.transition('closingRequest').modes()[0])
# n.transition('keepDown').fire(n.transition('keepDown').modes()[0])
# print(n.transition('entering0').modes())
# n.transition('raise').fire(n.transition('raise').modes()[0])
# print(n.place('p10').tokens)
# print(n.place('p20').tokens)
# print(n.place('p30').tokens)
# print(n.place('p1').tokens)
# print(n.place('p2').tokens)
# print(n.place('p3').tokens)
# print(n.place('p4').tokens)
# print(n.place('p5').tokens)
# print(n.place('p6').tokens)
# print(n.place('p7').tokens)
# print(n.place('p8').tokens)
# print(n.place('p9').tokens)


# from snakes.nets import *
# n = PetriNet('First net')
# n.add_place(Place('p', [3]))
# n.add_place(Place('a', [1]))
# n.add_transition(Transition('t', Expression('x>2&y>=0')))
# n.add_input('p', 't', Variable('x'))
# n.add_output('a', 't', Expression('y+1'))
# n.add_input('a', 't', Variable('y'))
# n.add_output('p', 't', Expression('x-1'))

# print(n.transition('t').modes())
# n.transition('t').fire(Substitution(x=3,y=1))
# print(n.place('p').tokens)
# print(n.place('a').tokens)


import pydot

graphs = pydot.graph_from_dot_file("graphs/lc_bp_v1.dot")
graph = graphs[0]
a = dict()
for i in graph.get_nodes():
    a[i.get_name()] = dict()

for i in graph.get_edges():
    a[i.get_source()][i.obj_dict['attributes']["label"]] = i.get_destination()

print(a)
# print(type(graph))
#print(graph.get_edges()[0].obj_dict['attributes']["label"])