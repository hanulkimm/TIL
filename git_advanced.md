# Git branch

## 개념
- 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구
- 장점: 독립 공간 형성하기 때문에 원본에 대해 안정함, 하나의 작업을 하나의 브랜치로 나누어 진행하므로 체계적인 개발 가능, 브랜치 만드는 속도가 빠르고 적응 용량 소모함

## git branch
### 조회
- `git branch`: 로컬 저장소의 브랜치 목록 확인
- `git branch -r` : 원격 저장소의 브랜치 목록 확인
### 생성
- ` git branch {branch 이름}`: 새로운 브랜치 생성
- ` git branch {branch 이름} {커밋 ID}`: 특정 커밋 기준으로 브랜치 생성
### 삭제
- `git branch -d {branch 이름}`: 병합된 브랜치만 삭제 가능
- `git branch -D {branch 이름}` : 강제 삭제

## git switch
- 현재 브랜치에서 다른 브랜치로 이동하는 명령어
- `git switch {branch 이름}` : {branch 이름} 브랜치로 이동
- `git switch -c {branch 이름}` : {branch 이름} 브랜치로 만들면서 이동
- `git branch {branch 이름} + git switch {branch 이름}`
- `git switch -c {branch 이름} {커밋 ID}`

- 주의! switch하기 전에, 해당 브랜치의 변경 사항을 반드시 커밋 해야함
  - 다른 브랜치에서 파일을 만들고 커밋 하지 않은 상태에서 switch하면 브랜치 이동했음에도 해당 파일이 그대로 남아있게 됨

## HEAD
- 현재 브랜치 가르킴
- 각 브랜치는 자신의 최신 커밋 가르킴
- 따라서, HEAD는 현재 브랜치의 최신 커밋을 가르킴

## 상태 파악
- `git log --all`: 모든 브랜치의 깃 로그 확인
- `git log --graph`: 깃 로그를 그림으로 확인
- `git log --oneline --all --graph`: 모든 브랜치의 깃 로그를 / 한줄로 / 그림으로 확인(명령어들의 조합)

## git merge
- `git merge {branch 이름}`
- 분기된 브랜치들을 하나로 합치는 명령어
- 병합하기 전에 브랜치를 합치려는 메인 브랜치로 switch 해야함
- 3가지 종류의 병합 존재
1. Fast-Forward
2. 3-way Merge: 각 브랜치의 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 방법

![image](https://user-images.githubusercontent.com/122726684/230522456-4d801e33-07c1-43d7-9cf6-e0546d97767d.png)

3. Merge conflict: 두 브랜치에서 같은 부분을 수정한 경우, git이 어느 브랜치 내용으로 작성해야 하는지 판단하지 못하여 발생하는 병합 방법, 같은 파일의 같은 부분을 수정했을 때 자주 발생함
  - 충돌이 발생한 부분은 작성자가 직접 해결해야함
  - 충돌 해결 후, 병합된 내용을 기록한 merge commit 생성
  
### VIM Editor
- vim editor에서
	- i : 입력모드
	- esc : 모드 취소
	- :wq : 저장 후 나가기