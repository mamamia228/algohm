#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long key;
    Node *l = nullptr, *r = nullptr;
    Node(long long k) : key(k) {}
};

Node* add(Node* t, long long x) {
    if (!t) return new Node(x);
    if (x < t->key) t->l = add(t->l, x);
    else if (x > t->key) t->r = add(t->r, x);
    return t;
}

Node* del(Node* t, long long x) {
    if (!t) return nullptr;
    if (x < t->key) t->l = del(t->l, x);
    else if (x > t->key) t->r = del(t->r, x);
    else {
        if (!t->l || !t->r) {
            Node* c = t->l ? t->l : t->r;
            delete t;
            return c;
        }
        Node* m = t->r;
        while (m->l) m = m->l;
        t->key = m->key;
        t->r = del(t->r, m->key);
    }
    return t;
}

bool exists(Node* t, long long x) {
    while (t) {
        if (x == t->key) return true;
        t = x < t->key ? t->l : t->r;
    }
    return false;
}

int height(Node* t) {
    return t ? 1 + max(height(t->l), height(t->r)) : 0;
}

void pre(Node* t, vector<long long>& out) {
    if (!t) return;
    out.push_back(t->key);
    pre(t->l, out);
    pre(t->r, out);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    Node* root = nullptr;
    while (q--) {
        string cmd;
        cin >> cmd;
        if (cmd == "add") { long long x; cin >> x; root = add(root, x); }
        else if (cmd == "del") { long long x; cin >> x; root = del(root, x); }
        else if (cmd == "exists") { long long x; cin >> x; cout << (exists(root, x) ? "YES" : "NO") << '\n'; }
        else if (cmd == "height") cout << height(root) << '\n';
        else if (cmd == "print") {
            if (!root) { cout << "Empty\n"; continue; }
            vector<long long> v;
            pre(root, v);
            for (size_t i = 0; i < v.size(); i++) cout << v[i] << (i + 1 < v.size() ? ' ' : '\n');
        }
    }
}
