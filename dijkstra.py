
class Node:
 def __init__(self, id=''):
  # unique identifier
  self.id = id
  # neighbors of this node
  self.neighbors = set()
  # distance to neighbors 
  self.length = dict()
  
 def addNeighbor(self, neighbor, distance):
  self.neighbors.add(neighbor)
  self.length[neighbor] = distance
  
 def getNeighbors(self):
  return set(self.neighbors)
 
 def getDistance(self, neighbor):
  if neighbor in self.neighbors:
   return self.length[neighbor]
  else:
   return float('inf')
   
 def getID(self):
  return self.id

def dijkstra(graph, source, destination):
 unvisitedNodes = set(graph)
 
 distance = dict()
 previousNode = dict()
 
 for node in unvisitedNodes:
  distance[node] = float('inf')
  previousNode[node] = None
 distance[source] = 0
 
 while destination in unvisitedNodes:
  minDistance = float('inf')
  for node in unvisitedNodes:
   if distance[node] < minDistance:
    minDistance = distance[node]
    currentNode = node
  
  # check that the minimum distance between unvisited and initial node is not infinity
  # float('inf') is float('inf') returns False
  if not minDistance is minDistance:
   return float('inf') # do something for nonexistant path
  unvisitedNodes.remove(currentNode)
  
  for neighbor in currentNode.getNeighbors():
   if neighbor not in unvisitedNodes:
    continue
   alt = distance[currentNode] + currentNode.getDistance(neighbor)
   if alt < distance[neighbor]:
    distance[neighbor] = alt
    previousNode[neighbor] = currentNode
 
 return distance, previousNode
 
 
import random

# Create nodes
N = 6
nodes = [Node('{0:3d}'.format(i + 1)) for i in range(N * N)]

# Print the nodes
for i in range(N):
 text = ''
 for j in range(N):
  text += nodes[i * N + j].getID()
 print(text)

# Arrange nodes in a grid, equidistant
for i in range(N * N - 1):
 if (i + 1) % N != 0:
  nodes[i].addNeighbor(nodes[i + 1], random.randint(1, N))
 if i // N < N - 1:
  nodes[i].addNeighbor(nodes[i + N], random.randint(1, N))

# Display nodes`
for i in range(N * N):
 attached = ''
 for node in nodes[i].getNeighbors():
  attached += node.getID() + ' '
 #print('Node %s is attached to %s' % (nodes[i].getID(), attached))

initialNode = nodes[0]
destination = nodes[-1]

distance, previousNode = dijkstra(nodes, initialNode, destination)

currentNode = destination
path = currentNode.getID()
while previousNode[currentNode] != None:
 path = previousNode[currentNode].getID() + ' -' + path
 currentNode = previousNode[currentNode]
print(path)
print(distance[destination])
