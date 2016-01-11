
class Node:
 def __init__(self, id=''):
  self.id = id
  self.attachedNodes = list()
 
 def addNode(self, pair):
  # pair is a node and distance to node tuple
  self.attachedNodes.append(pair)
  
 def getNodes(self):
  return self.attachedNodes
  
 def getID(self):
  return self.id

# Create nodes
N = 5
nodes = [Node(str(i)) for i in range(N * N)]

# Arrange nodes in a grid, equidistant
for i in range(N * N - 1):
 if (i + 1) % N != 0:
  nodes[i].addNode((nodes[i + 1], 1))
 if i // N < N - 1:
  nodes[i].addNode((nodes[i + N], 1))

# Display nodes`
for i in range(N * N):
 attached = ''
 for node in nodes[i].getNodes():
  attached += node[0].getID() + ' '
 print('Node %d is attached to %s' % (i, attached))

initialNode = nodes[0]
distance = dict({node:-1 for node in nodes})
distance[initialNode] = -1
visitedNodes = set({initialNode})

distance[nodes[0]] = 0