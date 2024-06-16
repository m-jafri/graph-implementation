from collections import defaultdict

class Graph:

    def __init__(self):

        self.adj_list_rep = defaultdict(list)

    def add_edge(self, src, dest):

        self.adj_list_rep[src].append(dest)
        return

    def bfs(self, src):

        raise NotImplementedError
    

    def dfs(self, src):

        raise NotImplementedError
    
