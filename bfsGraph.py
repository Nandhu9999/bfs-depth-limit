graph = {
  "a":["b","i","d"],
  "b":["a","h"],
  "c":["d","f","h"],
  "d":["a","c","e"],
  "e":["d","i"],
  "f":["c","g"],  
  "g":["f","x"],
  "h":["b","c"],
  "i":["a","e"],
  "x":["g"],
}

#   a - b - h
#   | \     |
#   i   d - c - f - g - x
#   | /
#   e

def bfs(graph,src,limit):
  v = [src]
  q = [src]
  lastElement = src
  
  while len(q) > 0 and limit > 0:
    ele = q.pop(0)

    for i in graph[ele]:
      if i not in v:
        q.append(i)
        v.append(i)

    if len(q) > 0 and ele == lastElement:        
      lastElement = q[-1]
      limit -= 1

  return v

limit = 1
print("\nlimit = ",limit)
for i in graph:
  lst = bfs(graph,i,limit)
  print(lst[0], lst[1:])
