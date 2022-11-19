    
    def print_all_paths_bfs(self, start, end):
        path = []
        print("All BFS path from {} to {} : ".format(start, end))
        self.__all_paths_bfs(start, end, path)


def main():    
    # 0 ----- 1
    #
    # 2 ---- 3 ---- 4

    # Disconnected graphs
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.disconnected_graphs_bfs()
    g.disconnected_graphs_dfs()
    g.disconnected_graphs_dfs_rec()
    g.print_all_paths_dfs(2, 4)
    g.print_all_paths_bfs(2, 4)
    print("***********************")

if __name__=="__main__":
    main()