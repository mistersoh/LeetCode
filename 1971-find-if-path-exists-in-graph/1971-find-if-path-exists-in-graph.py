class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def add_to_dict(dictionary,s,d):
            
            if s in dictionary:
                dictionary[s].append(d)
            else:
                dictionary[s] = [d]
        if n == 1:
            return True
            
        for lists in edges:
            if (lists[0] == source and lists[1] == destination) or (lists[1] == source and lists[0] == destination) :
                
                return True
        
        # Create dictionary of list of paths
        dict_of_path = dict()
        
        for lists in edges:
            add_to_dict(dict_of_path,lists[0],lists[1])
            add_to_dict(dict_of_path,lists[1],lists[0])
            
        if(source not in dict_of_path or destination not in dict_of_path):
            return False
        
        
        visited = set()
        paths = [source]
        
        while paths:
            
            # Current node
            node = paths.pop(0)
            
            # Check if current node able to reach to the destination
            if (destination in dict_of_path[node]):
                return True
            
            else:
                visited.add(node)
                
                for paths_able_to_go in dict_of_path[node]:
                    if paths_able_to_go not in visited:
                        paths.append(paths_able_to_go)
            
        return False