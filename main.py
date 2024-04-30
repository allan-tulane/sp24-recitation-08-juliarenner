from collections import deque
from heapq import heappush, heappop


def shortest_shortest_path(graph, source):

  shortest_path = {}

  for node in graph:
    shortest_path[node] = (float('inf'), 0)

  shortest_path[source] = (0, 0)
  lst = deque([source])

  while lst:
    node = lst.popleft()
    for neighbor, weight in graph[node]:
      if shortest_path[neighbor][0] > shortest_path[node][0] + weight:
        shortest_path[neighbor] = (shortest_path[node][0] + weight,
                                   shortest_path[node][1] + 1)
        lst.append(neighbor)
  return shortest_path


def bfs_path(graph, source):

  parents = {}

  for node in graph:
    parents[node] = None
  parents[source] = source
  lst = deque([source])
  while lst:
    node = lst.popleft()
    for neighbor in graph[node]:
      if parents[neighbor] is None:
        parents[neighbor] = node
        lst.append(neighbor)

  return parents


def get_sample_graph():
  return {'s': {'a', 'b'}, 'a': {'b'}, 'b': {'c'}, 'c': {'a', 'd'}, 'd': {}}


def get_path(parents, destination):
  path = []
  while destination != parents[destination]:
    destination = parents[destination]
    path.append(destination)
  return ''.join(reversed(path))
