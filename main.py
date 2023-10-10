# python3
# G = Bid Graph

class BidGraph:
    """Class of the Bid Graph, nodes are bids"""
    def __init__(self, bids):
        self.paths = []
        self.nodes = bids
        self.edges = []
    

    def __gen_path__(self, path, nodes):
        """Recursively generates all possible paths"""
        if len(nodes) == 0:
            return path
        else:
            path.append(nodes.pop(0))
            return self.__gen_path__(path, self.possible_bids(path))


    def gen_paths(self, nodes):
        """Generates all possible bid subsets"""
        
        for node in nodes:
            path = list()
            path.append(node)
            path = self.__gen_path__(path, self.possible_bids(path))
            self.paths.append(path)
        return 0

            
    def possible_bids(self, bids):
        """Returns all bids excluding bids with already taken items"""
        possible = []
        for bid in self.nodes:
            if not set.union(*bids).intersection(bid): # no intersection -> possible (item still available)
                possible.append(bid)
        return possible
    

            
                
        
    

def bob(G,g,MIN):
    pass


b = [("a"), ("b"), ("c"), ("d"), ("a", "b"), ("a", "c")]
b = [set(i) for i in b]
G = BidGraph(b)
print(G.possible_bids([{"a", "b"}, {"c"}]))
G.gen_paths((G.nodes))
print(G.paths)
