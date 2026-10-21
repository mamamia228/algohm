import sys

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])

    K = [0]   # ключи
    L = [0]   # левые дети (0 = нет)
    R = [0]   # правые дети
    H = [0]   # высоты (H[0] = 0 для пустого)
    keys = set()
    root = 0

    def upd(v):
        hl = H[L[v]]; hr = H[R[v]]
        H[v] = (hl if hl > hr else hr) + 1

    def rot_left(a):
        b = R[a]
        R[a] = L[b]
        L[b] = a
        upd(a); upd(b)
        return b

    def rot_right(a):
        b = L[a]
        L[a] = R[b]
        R[b] = a
        upd(a); upd(b)
        return b

    def balance(v):
        upd(v)
        bal = H[R[v]] - H[L[v]]
        if bal == 2:
            u = R[v]
            if H[R[u]] - H[L[u]] < 0:
                R[v] = rot_right(u)
            return rot_left(v)
        if bal == -2:
            u = L[v]
            if H[R[u]] - H[L[u]] > 0:
                L[v] = rot_left(u)
            return rot_right(v)
        return v

    def insert(t, x):
        if t == 0:
            K.append(x); L.append(0); R.append(0); H.append(1)
            return len(K) - 1
        if x < K[t]:
            L[t] = insert(L[t], x)
        else:
            R[t] = insert(R[t], x)
        return balance(t)

    out = []
    i = 1
    for _ in range(q):
        cmd = data[i]; i += 1
        if cmd == b"add":
            x = int(data[i]); i += 1
            if x not in keys:
                keys.add(x)
                root = insert(root, x)
        elif cmd == b"exists":
            x = int(data[i]); i += 1
            out.append("YES" if x in keys else "NO")
        elif cmd == b"root":
            out.append(str(K[root]) if root else "Empty")
        elif cmd == b"height":
            out.append(str(H[root]))
        else:  # print
            if not root:
                out.append("Empty")
                continue
            res = []
            stack = [root]
            while stack:
                v = stack.pop()
                res.append(K[v])
                if R[v]: stack.append(R[v])
                if L[v]: stack.append(L[v])
            out.append(" ".join(map(str, res)))

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))

main()
