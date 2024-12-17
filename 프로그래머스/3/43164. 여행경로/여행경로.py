from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    
    for start, end in tickets:
        graph[start].append(end)
        
    # 알파벳 순서로 출력하기 위해 역순 정렬
    for k in graph.keys():
        graph[k].sort(reverse=True)
        
    stack = ["ICN"]  # 시작 공항
    
    while stack:
        # 스택의 마지막 공항에 연결된 다른 공항이 있는 경우
        while graph[stack[-1]]:
            # 다음 목적지를 스택에 추가하고, 사용한 티켓은 제거
            stack.append(graph[stack[-1]].pop())
        # 더 이상 연결된 공항이 없는 경우, 결과에 추가
        answer.append(stack.pop())
        
    # 경로는 역순으로 저장되므로 반대로 뒤집어 반환
    return answer[::-1]