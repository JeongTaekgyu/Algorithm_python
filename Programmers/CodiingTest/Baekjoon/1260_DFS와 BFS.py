#import sys
#read = sys.stdin.readline()

def bfs_queue(adj_graph, start_node):

    queue = [start_node]    # 1. 시작 노드를 큐에 넣는다.
    visited = []

    while queue:
        current_node = queue.pop(0)     # 2-1. 맨 앞에서 빼겠다.
        visited.append(current_node)    # 2-2. 뺀 노드를 방문 노드에 넣는다.
        # 3. 현재 방문한 노드와 인전한 노드 중 방문하지 않은 노드를 큐에 추가한다.
        for adjacent_node in adj_graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)

    return visited


def dfs_stack(adjacent_graph, start_node):
    # 구현해보세요!
    stack = [start_node]
    visited = []

    # 스택이 비어있지 않을 때까지 반복한다.
    while stack:
        #현재 스택의 노드를 빼서 visited 에 추가한다.
        current_node = stack.pop()
        visited.append(current_node)
        #  현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 추가한다.
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)

    return visited

n, m, startVertex = map(int, input().split())
matrix = [ [0] * (n + 1) for i in range(n + 1) ]

visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1


print(dfs_stack(matrix, startVertex))
print(bfs_queue(matrix, startVertex))

