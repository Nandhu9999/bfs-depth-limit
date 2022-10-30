class node:
  def __init__(self,val) -> None:
    self.val = val
    self.left = None
    self.right = None

class tree:
  def __init__(self) -> None:
    self.root = node("root")

  def bfs(self,limit):
    if self.root == None:
      return

    q = [self.root]
    lastElement = self.root
    level = 1
    while len(q) > 0 and limit > 0:
      ele = q.pop(0)
      
      print(ele.val,"\t","[",level,"]")


      if ele.left != None:
        q.append(ele.left)

      if ele.right != None:
        q.append(ele.right)

      if len(q) > 0 and ele == lastElement:
        print("")
        lastElement = q[-1]
        level += 1
        limit -= 1

def main():
  t = tree()

  t.root.left = node("l1")
  t.root.right = node("r1")

  t.root.left.left = node("l1l2")
  t.root.left.right = node("l1r2")
  t.root.right.left = node("r1l2")
  t.root.right.right = node("r1r2")

  t.root.left.left.left = node("l1l2l3")
  t.root.left.left.right = node("l1l2r3")
  t.root.left.right.left = node("l1r2l3")
  t.root.left.right.right = node("l1r2r3")
  t.root.right.left.left = node("r1l2l3")
  t.root.right.left.right = node("r1l2r3")
  t.root.right.right.left = node("r1r2l3")
  t.root.right.right.right = node("r1r2r3")

  t.root.left.left.left.left = node("l1l2l3L4")
  t.root.left.left.left.right = node("l1l2l3R4")
  t.root.left.left.right.left = node("l1l2r3L4")
  t.root.left.left.right.right = node("l1l2r3R4")
  t.root.left.right.left.left = node("l1r2l3L4")
  t.root.left.right.left.right = node("l1r2l3R4")
  t.root.left.right.right.left = node("l1r2r3L4")
  t.root.left.right.right.right = node("l1r2r3R4")

  t.root.right.left.left.left = node("r1l2l3L4")
  t.root.right.left.left.right = node("r1l2l3R4")
  t.root.right.left.right.left = node("r1l2r3L4")
  t.root.right.left.right.right = node("r1l2r3R4")
  t.root.right.right.left.left = node("r1r2l3L4")
  t.root.right.right.left.right = node("r1r2l3R4")
  t.root.right.right.right.left = node("r1r2r3L4")
  t.root.right.right.right.right = node("r1r2r3R4")

  t.bfs(limit=4)

if __name__ == "__main__":
  main()
