import sys
input = sys.stdin.readline

def count_leaf(node, tree):
    if not tree[node]:
        return 1
    count = 0
    for child in tree[node]:
        count += count_leaf(child, tree)
    return count
    

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    delete_node = int(input())  
    
    tree = [[] for _ in range(n)]
    root = -1
    for node, parent in enumerate(parents):
        if parent == -1:
            root = node
        else:
            tree[parent].append(node)
            
    if delete_node == root:
        print(0)
        return
    
    parent = parents[delete_node]
    tree[parent].remove(delete_node)
     
    print(count_leaf(root, tree))
    

if __name__ == "__main__":
    main()