class Solution:
  def __init__(self, nodes, target_node, passing_node):
    # Initialise graph with no vertices and edges.
    self.graph = []

    for i in range(len(nodes)):
      self.graph.append([])
      for _ in range(len(nodes)):
        self.graph[i].append(0)

    # Create nodes in graph.
    for node1, node2, weight in nodes:
      # Following 0 indexing.
      self.graph[node1][node2] = weight
      self.graph[node2][node1] = weight

    self.no_nodes = len(nodes)
    self.target_node = target_node
    self.passing_node = passing_node
    self.path = None
    self.dist = 0
    self.solution_exist = False
    self.visited = [False for _ in range(len(nodes))]


  def dfs(self, starting_node, path=[], dist=0):
    if starting_node == self.target_node and \
      self.passing_node in path:
      path.append(starting_node)
      # For first path found or if a new path with lesser distance
      # is found then use the new path and distance.
      if not self.solution_exist or dist < self.dist:
        self.path = path[:]
        self.dist = dist
        self.solution_exist = True
    
    for node in range(starting_node, self.no_nodes):
      self.visited[node] = True
      for adj_node in range(self.no_nodes):
        # For each unvisited adjacent node perform dfs to find target node.
        if self.graph[node][adj_node] != 0 and not self.visited[adj_node]:
          path.append(node)
          dist += self.graph[node][adj_node]
          self.dfs(adj_node, path, dist)
          dist -= self.graph[node][adj_node]
          path.pop()


  def solve(self, starting_node):
    self.dfs(starting_node)
    if self.solution_exist:
      print(f"\nShortest path = {self.dist}")
      print("Path taken = ", end="")
      for node in self.path:
        print(node+1, end=" ")
    else:
      print("\nNo path found")


def main():
  no_nodes = int(input("N = "))
  lines = []
  print("\nP Q D")
  for _ in range(no_nodes):
    line = input()
    (node1, node2, dist) = line.split(' ')
    lines.append((int(node1)-1, int(node2)-1, int(dist)))
  print()
  starting_node = int(input("A = ")) - 1
  passing_node = int(input("B = ")) - 1
  target_node = int(input("C = ")) - 1
  s = Solution(lines, target_node=target_node, passing_node=passing_node)
  s.solve(starting_node)

if __name__ == "__main__":
  main()