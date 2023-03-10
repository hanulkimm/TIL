# 트리 Tree

## 정의
- 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건 만족
  - 노드 중 최상위 노드를 루트
  - 나머지 노드들은 분리 집합으로 분리
- 분리 집합은 하나의 트리가 되며 루트의 부 트리라 한다
## 용어
- 노드 : 트리의 원소
- 간선: 노드를 연결하는 선, 부모 노드와 자식 노드를 연결
- 루트 노드: 트리의 시작 노드
- 형제 노드: 같은 부모 노트의 자식 노드들
- 조상 노드: 간선을 따라 루트 노트까지 이르는 경로에 있는 모든 노드들
- 서브 트리(subtree): 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드: 서브 트리에 있는 하위 레벨의 노드들
  
### 차수
- 노드의 차수: 노드에 연결된 자식 노드의 수 
- 트리의 차수: 트리에 있는 

### 높이
- 노드의 높이: 루트에서 노드에 이르는 간선의 수, 노드의 레벌
- 트리의 높이: 트리에 있는 노드의 높이 중에서 가장 큰 값, 최대 레벨

## 트리의 종류
### 이진 트리
- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대 2개까지만 가질 수 있는 트리
- 레벨 i에서의 노드의 최대 개수는 2^i개(i=0,1,2, ...)
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개가 되며, 최대 개수는 2^(h+1)-1 개가 된다
  
### 포화 이진 트리 (Full Binary Tree)
- 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 높이가 h일 때, 최대 노드 개수인 2^(h+1)-1 개를 가진 이진 트리
- 루트를 1번부터 하여 2^(h+1)-1까지 정해진 위치에 대한 노드 번호를 가짐

### 완전 이진 트리 (Complete Binary Tree)
- 높이가 h이고 노드 수가 n개 일 때(2^h <= n < 2^(h+1)-1), 포화 이진 트리의 노드 번호 1번 부터 n번까지 빈 자리가 없는 이진 트리

### 편향 이진 트리 (Skewed Binary Tree)
- 높이 h에 대한 최소 개수의 노드를 사지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
  - 왼쪽 편향 이진 트리
  - 오른쪽 편향 이진 트리

# 순회
## 순회란?
- 트리의 각 노드를 중복되지 않게 전부 방문하는 것을 말하는데 트리는 비 선형 구조이기 때문에 선형구조와 같이 선후 연결관계를 알 수 없다
- 순회: 트리의 노드들을 체계적으로 방문하는 것

## 3가지 기본적인 순회 방법
### 전위 순회(preorder traversal): VLR
- 부모노드 방문 후, 자식노드를 좌, 우 순서로 방문
```python
def preorder_traverse(n):
    if n:
        visit(n)
        preorder_traverse(left[n])
        preorder_traverse(right[n])
```
### 중위 순회(inorder traversal): LVR
- 왼쪽 자식 노드, 부모 노드, 오른쪽 자식노드 순으로 방문(왼쪽에서 return할때 처리해주기)
```python
def inorder_traverse(n):
    if n:
        inorder_traverse(left[n])
        visit(n)
        inorder_traverse(right[n])
```
### 후휘 순회(postorder traversal)
- 자식 노드를 좌우 순서로 방문한 후, 부모노드로 방문
```python
def postorder_traverse(T):
    if T:
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)
```

## 이진트리의 표현
### 노드 번호의 성질
- 노드 번호가 i인 노드의 부모 번호: i // 2
- 노드 번호가 i인 노드의 왼쪽 노드 번호: 2*i
- 노드 번호가 i인 노드의 오른쪽 노드 번호: 2*i+1

## 이진트리의 저장
### 부모 번호를 인덱스로 자식 번호를 왼쪽, 오른쪽 저장
```python
p, c
if left[p]==0:
    left[p]==c
else:
    right[p]==c
```
### 자식 번호를 인덱스로 부모 번호를 저장
- 조상 노드 찾고 싶을 때, 루트를 찾고 싶을 때 유용
```python
p = [0] * (V+1)
par[c] = p
c = 5 # 조상 노드 찾기
while p[c]!=0:
    c = p[c]
    anc.append(c)
root = c
```

# 이진 탐색 트리
- 탐색 작업을 효율적으로 하기 위한 자료구조
- 모든 원소는 서로 다른 유일한 키 가짐
- key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
- 중위 순회하면 오름차순으로 정렬된 값 얻을 수 있음

# 힙
- 완전이진트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해서 만든 자료 구조
## 최대 힙
- 키값이 가장 큰 노드를 찾기 위한 완전 이진 트리
- 부모노드의 키 값 > 자식노드의 키 값
- 루트 노드: 키값이 가장 큰 노드

