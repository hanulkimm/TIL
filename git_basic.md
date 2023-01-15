# Git basic

## What is Git?
-'깃' (git)이란?  
 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한  분산 버전 관리 시스템이다. 

 ## Basic Git Commands
 - Insert user information to git  
    - `git config --global user.name "name"`  
    - `git config --global user.email ~.com`

- Create git repository  
    - `git init`

- Add files
  - `git add .` (모든 파일 add 하기)
  - `git add {file name}`

- Commit 
  - `git commit -m '{message}'`

- Push
  - `git push origin master`
  - `git push -u origin master`   
  이후 origin master 생략 가능

- Status
  - `git status` 

- Check commit(Log)
  - `git log`
  - `git log --oneline --graph`

- Connect remote repository
  - `git remote add origin {url}`   
  : 'origin' 다르게 설정 가능, 그러나 권장하지 않음
  - `git remote -v`
  : 원격 저장소의 상세 정보

-  Push
   - `git push origin master`
   - `git push -u origin master`

- Pull
  - `git pull origin master`
  - `git pull -u origin master`

- Clone
  - `git clone {url}`

- Amend Commit
  - `git commit --amend`  
  : vim editor 등장, i for insert, esc for mode out, :wq for save and out

- Make ignore folder
  - `.gitignore  `  
  : git에서 관리하지 않는 파일/폴더의 모음  
  : txt 만들어서 git에 올리고 싶지 않은 파일명들 적음  
  : 항상 commit해서 push 해야 됨  
  : gitignore.io 사용하기

- Reset commit 
  - `git reset --hard {commit id}`   
  : 스켈레톤 코드 사용할 경우만 사용하기

- Commit list 
  - `git reflog`  
	: 깃 커밋 변경사항 리스트


