# Capstone-Design
졸업작품 - 퀴즈 게임

실행하실 때   
1. pip install -r requirements.txt로 필요한 라이브러리들을 받습니다.
2. python manage.py makemigrations, migrate로 db가 만들어졌는지 확인합니다.
3. python manage.py createsuperuser로 장고 관리자를 만듭니다.
4. 장과 관리자 페이지로 들어가서 Quizs 탭에 들어가셔서 추가를 누릅니다.    
(예제 사진 파일은 저희가 올려드린 readme_picture폴더의 Quiz_picture에 있습니다.Quiz_picture에 1번~5번 폴더를 참조하셔서
아래의 사진처럼 추가해주시면 될 것 같습니다.   
다른 사진들로 테스트 해보시려면 Quiz 오브젝트 5개를 지우신 후에 opencv 폴더 안의 img(원본파일 폴더)와 다른 폴더(opencv 처리된 폴더)에서 아래의 사진과 같이 추가하시면 됩니다.)   
아래와 같이 만든 후 저장한 다음에 장고 관리자 페이지에서 로그아웃 후 다시 터미널로 돌아옵니다.
![1번_퀴즈](readme_picture/img.png)
![2번_퀴즈](readme_picture/img_1.png)
![3번_퀴즈](readme_picture/img_2.png)
![4번_퀴즈](readme_picture/img_3.png)
![5번_퀴즈](readme_picture/img_4.png)
5. python manage.py runserver 로 페이지를 실행시킵니다.
6. 유저를 생성하시고 방을 생성하신 다음에 4번에서 만든 페이지로 실행 결과를 확인하실 수 있습니다.
