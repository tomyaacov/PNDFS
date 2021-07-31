import pydot

class BPGraph:
    def __init__(self, file_path):
        file = open(file_path, "r")
        content = file.readlines()
        all_contents = "\n".join(content)
        self.start = all_contents[all_contents.find("  -1 -> ")+8]
        wo_start_content = [x for x in content if not x.startswith("  -1")]
        graphs = pydot.graph_from_dot_data("\n".join(wo_start_content))
        graph = graphs[0]
        self.graph = dict()
        for i in graph.get_nodes():
            self.graph[i.get_name()] = dict()

        for i in graph.get_edges():
            self.graph[i.get_source()][i.obj_dict['attributes']["label"][1:-1]] = i.get_destination()
        

