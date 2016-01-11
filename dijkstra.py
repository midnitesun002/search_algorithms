
class Node:
 def __init__(self, id=''):
  self.id = id
  self.attachedNodes = list()
 
 def addNode(self, pair):
  # pair is a node and distance to node tuple
  self.attachedNodes.append(pair)
  
 def getNeighbors(self):
  return self.attachedNodes
  
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
distance = dict({node:-1 for node in nodes})
distance[initialNode] = 0
unvisitedNodes = set({node for node in nodes if node is not initialNode})

currentNode = initialNode
for neighbor in currentNode.getNeighbors():
 