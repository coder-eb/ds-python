class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def __str__(self) -> str:
        SPACES = 4

        str_rep = "{\n"
        for vertex, edges in self.adj_list.items():
            str_rep += " " * SPACES
            str_rep += f"{vertex}: {edges},"
            str_rep += "\n"
        str_rep += "}"
        return str_rep
