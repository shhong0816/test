import pandas as pd

atom 위 설정에서 package들어가서 서 toggle github tab실행.

#https://www.youtube.com/watch?v=3d8waEqZZI8&ab_channel=You_Blue

폴더 제작 후 C:\Program Files\Git 의 git-cmd실행
이후 폴더 경로로 이동. 여기 같은경우 D:\python\git\test 까지
이후 아래꺼 입력.
이때 폴더 경로랑 site경로는 원하는 곳으로 내가 설정 한번 해줘야함.

echo "# Atom" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin "https://github.com/shhong0816/test.git"
git push -u origin master

이러면 연동된거

이후 오른쪽 github tab에서 코드 변경후 stage all 클릭. commit to master클릭 (commit message optional)

아래에 기록들 뜨면서 github site가면 수정임.

Changelog1
