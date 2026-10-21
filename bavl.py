import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    keys = [int(data[idx + i]) for i in range(n)]
    idx += n
    m = int(data[idx]); idx += 1

    left, right, parent = {}, {}, {}
    root = None

    for k in keys:
        left[k] = right[k] = None
        if root is None:
            root = k
            parent[k] = None
            continue
        cur = root
        while True:
            if k < cur:
                if left[cur] is None:
                    left[cur] = k
                    break
                cur = left[cur]
            else:
                if right[cur] is None:
                    right[cur] = k
                    break
                cur = right[cur]
        parent[k] = cur

    out = []
    for _ in range(m):
        cmd = data[idx]; a = int(data[idx + 1]); idx += 2
        p = parent[a]
        if cmd == "left":
            b = right[a]
            mid = left[b]
            right[a] = mid
            if mid is not None:
                parent[mid] = a
            left[b] = a
        else:
            b = left[a]
            mid = right[b]
            left[a] = mid
            if mid is not None:
                parent[mid] = a
            right[b] = a
        parent[a] = b
        parent[b] = p
        if p is None:
            root = b
        elif left[p] == a:
            left[p] = b
        else:
            right[p] = b

        res = []
        stack = [root]
        while stack:
            v = stack.pop()
            res.append(v)
            if right[v] is not None:
                stack.append(right[v])
            if left[v] is not None:
                stack.append(left[v])
        out.append(" ".join(map(str, res)))

    print("\n".join(out))

main()
