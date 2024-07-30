pjt 파일의 urls 에서 app.urls로 다시 경로 보내기
요청한 경로에 url(articles)의 이름이 들어오면 하위 urls로 다시 보내서 실행 
pjt파일 urls.py 코드
```python
path('articles/', include('articles.urls')
```
app.urls 

최상단 urls에서 앞의 url이름이 포함되면 하위 urls로 경로 보냄
유지보수편하기 위해 분리 작업


# html 통합관리 
{% extends 'base.html' %} app templates의 html 파일 (상속)

{% block body %}
{% endblock %}    
base와 상속받을 .html 파일 모두 작성   
base파일의 블럭에 상속받은 html파일의 블럭을 넣는 개념   

## 장고에 설정값을 수정하여 app 안의 templates와 상위폴더의 templates도 실행할 수 있도록 함

settings.py Tempaltes 'DIRS': [BASE_DIR(최상위폴더) / 'templates']


BASE_DIR = Path(__file__).resolve().parent.parent
            경로(settings.py위치기준).부모.부모(상위폴더)


모델링(스키마정의)
데이터 타입과 데이터 구조 정의 
