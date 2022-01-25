# movie

ㅇ 작성 일자: 21.1.25

ㅇ 요구 사항
MSA는 다음 역할을 수행하는 컨테이너로 구성해야 합니다.
UI 컨테이너: UI의 틀을 구성하는 컨테이너
영화 정보 컨테이너: 영화 정보를 제공하는 컨테이너
영화 카드를 클릭하면 영화 관련 상세 정보를 나타내야 합니다.
영화 스트리밍 기능은 만들지 않습니다.
제목, 설명 등으로 이루어진 간소한 페이지로 구성하면 됩니다.
데이터베이스는 필수가 아니나 원하는 경우에 구성할 수 있습니다.
코드를 구성하는 언어는 어느 것을 사용해도 무관하나 영화 정보 컨테이너는 기본적인 RestAPI의 구성을 갖춰야 합니다.

ㅇ 작성 결과
1. frontend : web ui를 위한 flask app.py 로 구성, html, css 등의 static file 과 Dockerfile 포함 
2. backend : 영화 정보를 제공하는 Rest API 관련 flask app.py 로 구성, Dockerfile 포함
3. kubernetes : frontend container와 backend container의 pod, service 배포를 위한 yaml 파일 및 ingress 배포를 위한 정책 파일
