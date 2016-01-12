
class Node:
 def __init__(self, id=''):
  self.id = id
  self.attachedNodes = list()
 
 def addNode(self, pair):
  # pair is a node and distance to node tuple
  self.attachedNodes.append(pair)
  
 def getNeighbors(self):
  return self.attachedNodes[:]
  
 def getID(self):
  return self.id

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
  nodes[i].addNode((nodes[i + 1], 1))
 if i // N < N - 1:
  nodes[i].addNode((nodes[i + N], 1))

# Display nodes`
for i in range(N * N):
 attached = ''
 for node in nodes[i].getNeighbors():
  attached += node[0].getID() + ' '
 print('Node %s is attached to %s' % (nodes[i].getID(), attached))

initialNode = nodes[0]
destination = nodes[-1]

distance = dict({node:float('inf') for node in nodes})
distance[initialNode] = 0

currentNode = initialNode
unvisitedNodes = set(nodes)

while destination in unvisitedNodes:
 for neighbor in currentNode.getNeighbors():
  if neighbor[0] not in unvisitedNodes:
   continue
  if distance[currentNode] + neighbor[1] < distance[neighbor[0]]:
   distance[neighbor[0]] = distance[currentNode] + neighbor[1]
 unvisitedNodes.remove(currentNode)
 
 minDistance = float('inf')
 for node in unvisitedNodes:
  if distance[node] < minDistance:
   minDistance = distance[node]
   currentNode = node
 
 # check that the minimum distance between unvisited and initial node is not infinity
 # float('inf') is float('inf') returns False
 if not minDistance is minDistance:
  break
 


print(distance[destination])