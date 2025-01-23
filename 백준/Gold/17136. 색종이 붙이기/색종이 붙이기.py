import sys
input = sys.stdin.readline
INF = int(1e9)

def calc_min_paper(paper, n):
    paper_count = [0, 5,5,5,5,5]  # 종이 크기별 사용 가능한 개수
    
    # 종이를 붙이거나(0) 제거함(1)
    def update_paper(x, y, size, status):
        for i in range(x, x + size):
            for j in range(y, y + size):
                paper[i][j] = status
    
    # 종이 범위를 벗어나거나 0인 곳에는 붙일 수 없음
    def can_attach(x, y, size):
        if x + size > n or y + size > n:
            return False
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] == 0:
                    return False
        return True
     
    def backtrack(count):
        nonlocal min_count
        
        for i in range(n):
            for j in range(n):
                if paper[i][j] == 1:
                    break
            else:
                continue
            break
        else:
            min_count = min(min_count, count)
            return
        
        for i in range(n):
            for j in range(n):
                if paper[i][j] == 1:  # 덮을 위치를 찾고, 큰 종이부터 시도
                    for size in range(5, 0, -1):
                        # 종이가 남아있고, 붙일 수 있는 경우
                        if paper_count[size] > 0 and can_attach(i, j, size):
                            update_paper(i, j, size, 0)
                            paper_count[size] -= 1
                            backtrack(count + 1)
                            update_paper(i, j, size, 1)
                            paper_count[size] += 1
                    return 
        
    min_count = INF
    backtrack(0)
    
    return min_count if min_count != INF else -1


def main():
    paper = [list(map(int, input().split())) for _ in range(10)]
    print(calc_min_paper(paper, len(paper)))


if __name__ == "__main__":
    main()