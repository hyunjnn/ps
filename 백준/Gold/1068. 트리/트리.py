import sys
input = sys.stdin.readline

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    delete_node = int(input())  
    
    # 각 노드별 자식 리스트
    tree = [[] for _ in range(n)]
    root = -1
    for node, parent in enumerate(parents):
        if parent == -1:
            root = node
        else:
            tree[parent].append(node)
    
    # 루트를 삭제하면 리프 노드는 없음
    if delete_node == root:
        print(0)
        return
    
    # 노드 삭제
    # def delete_subtree(node):
    #     for child in tree[node]:
    #         delete_subtree(child)
    #     tree[node] = []
    parent = parents[delete_node]
    # # if parent != -1:
    tree[parent].remove(delete_node)
    # delete_subtree(delete_node)
    
    # 리프 노드 카운트
    def count_leaf(node):
        if node == delete_node:
            return 0
        if not tree[node]:
            return 1
        count = 0
        for child in tree[node]:
            count += count_leaf(child)
        return count
    
    print(count_leaf(root))
    

if __name__ == "__main__":
    main()