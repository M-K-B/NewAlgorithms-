


class Graph(object):
    
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])   
        self.size = size


    #methods for (1) adding a vertex; (2) adding an edge; (3) removing an edge; and (4) printing the
    #matrix should appear here

    def add_vertex(self):
        self.adjMatrix.append([0 for i in range(self.size)])
        for i in range(self.size):
            self.adjMatrix[i].append(0)
        self.size += 1
             

        

    def add_edge(self, a, b): # defines adding an edge with self , a and b 
        if a == b: # if a is equal to  b 
            print(a,b) # print a , b 
        self.adjMatrix[a-1][b-1] = 1 # calls adjMatrix with index a - 1 index b-1 and assigns it 1
        self.adjMatrix[b-1][a-1] = 1 # calls adjMatrix with index b-1 index a - 1 and assigns it 1
    
    def remove_edge(self, a, b):   # defines remove  with self , a and b 
        if self.adjMatrix[a-1][b-1] == 0: # if the value of the adjMatrix is 0 return 
            return 
        else: 
            self.adjMatrix[a-1][b-1] = 0# calls adjMatrix with index a - 1 index b-1 and assigns it 0
            self.adjMatrix[b-1][a-1] = 0#calls adjMatrix with index b-1 index a - 1 and assigns it 0

    def print_matrix (self):                                                # Define the function for Priting the matrix
        Graph_grid = "    "                                                 # Create a string that cotains some tabs as characters
        Dash = "    ------------------"                                     # String of dashs
        for a in range(self.size - 1):                                      # for loop to count up to the size graph 
            Graph_grid += f" {a + 1} "                                      # 
                                                                            # string plus all the number to the assigned to self.size will show horizontally 
        
        Graph_grid += "\n" # new line 
        Graph_grid += f"{Dash}" # add the dash to the graph that seprate the number of 0 and 1's
        
        
        for a in range(self.size - 1): # for loop that goes through the list of how long the graph is 
            Graph_grid += f"\n {a + 1} |"  # displays the 0's and 1's 
            
            for b in range(self.size - 1): # for loop that goes through the list of how long the graph is 
                Graph_grid += f" {self.adjMatrix[a][b]} "  # displays the 0's and 1's from the adjactimatrix fucntoon 
            Graph_grid += "\n" # new line 
        print(Graph_grid)    # the grid     
    
#remember list indexing - this is 1 out, unless we start the matrix at 0 (not a +ve integer)     
def main():
        g = Graph(6)
        
        g.add_vertex()
        g.add_vertex()
        g.add_vertex()
        
        
        
        g.add_edge(1,2)
        g.add_edge(1,3)
        g.add_edge(2,3)
        g.add_edge(3,4)
        g.add_edge(5,6)

        g.remove_edge(5,6)
        
        g.add_edge(2,4)
        
        
        g.print_matrix()
        

if __name__ == '__main__':
   main()
