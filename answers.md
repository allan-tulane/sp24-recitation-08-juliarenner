# CMPS 2200 Recitation 08

## Answers

**Name:** Julia Renner


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**
- 
- The work of my algorithm is O(V+E * logV)
- The span of my algorithm is O(V+E)
- 
- **2b)**
- 
- def get_path(parents, destination):
  - path = []
  - while destination != parents[destination]:
    - destination = parents[destination]
    - path.append(destination)
  - return ''.join(reversed(path))
