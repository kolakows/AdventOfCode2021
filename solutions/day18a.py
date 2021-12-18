import ast


class ValNode:

    def __init__(self, val, parent, depth):
        self.val = val
        self.parent = parent
        self.depth = depth

    def split(self):
        replacement = AddNode([self.val//2, (self.val+1)//2], self.parent, self.depth)
        for i in range(2):
            if self.parent[i] == self:
                self.parent[i] = replacement

    def closest_node(self, side) -> "ValNode":
        parent = self.parent
        current_node = self
        opposing_node = None
        # find parent node where side child is on other path from root
        while parent:
            if parent[1-side] is current_node:
                opposing_node = parent[side]
                break
            current_node = parent
            parent = parent.parent
        if opposing_node:
            while isinstance(opposing_node, AddNode):
                opposing_node = opposing_node[1-side]
        return opposing_node

    def tolist(self):
        return self.val

    def value(self):
        return self.val


class AddNode:
    def __init__(self, children, parent, depth):
        self.parent = parent
        self.depth = depth

        self.children = []
        for c in children:
            if isinstance(c, int):
                self.children.append(ValNode(c, self, depth + 1))
            else:
                self.children.append(AddNode(c, self, depth + 1))

    def __getitem__(self, item):
        return self.children[item]

    def __setitem__(self, key, value):
        self.children[key] = value

    def explode(self):
        for i in range(2):
            nb = self[i].closest_node(i)
            if nb:
                nb.val += self[i].val
        for i in range(2):
            if self.parent[i] is self:
                self.parent[i] = ValNode(0, self.parent, self.depth)

    def value(self):
        v = 0
        for i in range(2):
            v += (3-i) * self[i].value()
        return v

    def tolist(self):
        return [self[0].tolist(), self[1].tolist()]


def split(node):
    if isinstance(node, ValNode) and node.val >= 10:
        node.split()
        return True
    if isinstance(node, AddNode):
        for i in range(2):
            if split(node[i]):
                return True


def explode(node):
    if isinstance(node, AddNode) and node.depth == 4:
        node.explode()
        return True
    if isinstance(node, AddNode):
        for i in range(2):
            if explode(node[i]):
                return True
    return False


def reduce(node):
    while explode(node) or split(node):
        pass


with open('input.txt') as f:
    data = f.read()

numbers = list(map(ast.literal_eval, data.splitlines()))
root = AddNode(numbers[0], None, 0)
for n in numbers[1:]:
    q = [root.tolist(), n]
    root = AddNode(q, None, 0)
    print(root.tolist())
    reduce(root)
print(root.tolist())
print(root.value())
