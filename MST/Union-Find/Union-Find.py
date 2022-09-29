# == 서로소 집합 == 상호 배타 집합 == Disjoint Set

# 1. 반복문
def find_set(node):
    while node != parent[node]:                         # node == parent[node]이면 node가 대표값
        node = parent[node]
    return node


# # 2. 재귀
# def find_set(node):
#     if node != parent[node]:
#         return find_set(parent[node])
#     return node


# # 3. 재귀 - 경로 압축(부모 노드를 대표값으로 만듦)
# parent 리스트 안의 값을 대표값으로 다 바꿔주기 때문에 처음 한번은 비효율적일지 몰라도 다음부터 굉장히 빨라진다.
# def find_set(node):
#     if node != parent[node]:
#         parent[node] = find_set(parent[node])
#     return parent[node]


n, m = map(int, input().split())                        # 정점, 간선(Union 횟수) 개수
parent = list(range(n + 1))                             # make_set(원소는 부모를 가리킴) -> parent = [0, 1, 2, 3, 4, 5, 6]

for _ in range(m):
    x, y = map(int, input().split())
    x_root, y_root = find_set(x), find_set(y)  # Find

# Find의 속도가 줄면 Union도 빨라짐
#

# Union(1, 3) 하는 과정
# 1. 각 숫자가 속한 집합의 대표값을 구한다. -> Union(1, 3)
# 2. 같은 집합인지 확인
# 3. 합친다.
# parent = [0, 1, 2, 1, 4, 5, 6]
# 1에다가 3을 붙일지 3에다가 1을 붙일지 결정해야하는데,
# 보통 작은숫자에 큰 숫자를 붙여준다.

# 이후 Union(2, 3)
# 1. 3이 속한 집합의 대표값 : 1  -> Union(2, 1)
# 2. 같은 집합인지 확인
# 3. 합친다.
# parent = [0, 1, 1, 1, 4, 5, 6]

    # Union
    if x_root != y_root:  # 서로소 집합인 경우만 합집합 연산
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root

# 출력
for i in range(1, n + 1):
    print(find_set(i), end=' ')

print()
print(parent)