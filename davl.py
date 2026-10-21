import sys


class Node:
    __slots__ = ("key", "left", "right", "height")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    return node.height if node else 0


def update(node):
    node.height = max(height(node.left), height(node.right)) + 1


def balance_factor(node):
    return height(node.right) - height(node.left)


def rotate_left(a):
    b = a.right
    a.right = b.left
    b.left = a
    update(a)
    update(b)
    return b


def rotate_right(a):
    b = a.left
    a.left = b.right
    b.right = a
    update(a)
    update(b)
    return b


def rebalance(v):
    update(v)
    bal = balance_factor(v)
    if bal == 2:
        if balance_factor(v.right) < 0:
            v.right = rotate_right(v.right)
        return rotate_left(v)
    if bal == -2:
        if balance_factor(v.left) > 0:
            v.left = rotate_left(v.left)
        return rotate_right(v)
    return v


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node
    return rebalance(node)


def remove_min(node):
    """Удаляет минимальную вершину поддерева и балансирует путь вверх."""
    if node.left is None:
        return node.right
    node.left = remove_min(node.left)
    return rebalance(node)


def delete(node, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if node.left is None or node.right is None:
            return node.left or node.right
        m = node.right
        while m.left:
            m = m.left
        node.key = m.key
        node.right = remove_min(node.right)
    return rebalance(node)


def exists(node, key):
    while node:
        if key == node.key:
            return True
        node = node.left if key < node.key else node.right
    return False


def next_key(node, key):
    """Минимальный ключ >= key."""
    best = None
    while node:
        if node.key >= key:
            best = node.key
            node = node.left
        else:
            node = node.right
    return best


def prev_key(node, key):
    """Максимальный ключ <= key."""
    best = None
    while node:
        if node.key <= key:
            best = node.key
            node = node.right
        else:
            node = node.left
    return best


def preorder(root):
    result = []
    stack = [root] if root else []
    while stack:
        v = stack.pop()
        result.append(v.key)
        if v.right:
            stack.append(v.right)
        if v.left:
            stack.append(v.left)
    return result


def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    pos = 1
    root = None
    out = []

    for _ in range(q):
        cmd = data[pos].decode()
        pos += 1

        if cmd in ("add", "del", "exists", "next", "prev"):
            x = int(data[pos])
            pos += 1

        if cmd == "add":
            root = insert(root, x)
        elif cmd == "del":
            root = delete(root, x)
        elif cmd == "exists":
            out.append("YES" if exists(root, x) else "NO")
        elif cmd == "next":
            res = next_key(root, x)
            out.append("None" if res is None else str(res))
        elif cmd == "prev":
            res = prev_key(root, x)
            out.append("None" if res is None else str(res))
        elif cmd == "root":
            out.append(str(root.key) if root else "Empty")
        elif cmd == "height":
            out.append(str(height(root)))
        elif cmd == "print":
            keys = preorder(root)
