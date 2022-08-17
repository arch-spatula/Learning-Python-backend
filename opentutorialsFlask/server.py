from flask import Flask
import random

app = Flask(__name__)

# 아래 리스트는 데이터 베이스로 제어하는 것이 좋다. 
Topics = [
    {'id' : 1, 'title': 'HTML', 'body' : 'html is ...'},
    {'id' : 2, 'title': 'CSS', 'body' : 'CSS is ...'},
    {'id' : 3, 'title': 'JavaScript', 'body' : 'JavaScript is ...'}
]

def Template(contents, content):
    return f'''<!DOCTYPE html>
    <html lang="ko">
    <head>
        <title>Document</title>
    </head>
    <body>
        <h1><a href="/">Web</a></h1>    
        <ol>
            {contents}
        </ol>
        {content}
    </body>
    </html>
    '''

def getContents():
    liTags = ''
    for Topic in Topics:
        liTags += f'<li><a href="/read/{Topic["id"]}/">{Topic["title"]}</a></li>'
    return liTags

@app.route('/')  #여기 줄은 데이코레이터이다. 여기 주소를 입력하면 아래 내용으로 응답해준다. 
def index():
    return Template(getContents(), '<h2>Welcome</h2> Hello, Web!')

@app.route('/create')
def create():
    return 'create'

# <>에 해당하는 것을 아래 파라미터로 넣으면 같은 형식의 내용이 다른 여러 페이지를 볼 수 있다. 
# <int: id>라고 하면 id는 자료형이 정수가 된다.
@app.route('/read/<int:id>/')  
def read(id):
    title = ''
    body = ''
    for Topic in Topics:
        if id == Topic['id']:  # 조회하기
            title = Topic['title']
            body = Topic['body']
    return Template(getContents(), f'<h2>{title}</h2>{body}')
#  <h2>{title}</h2>
        # {body}


if __name__ == "__main__":
    app.run(port=3000, debug=True)  # 개발 중에는 debug=True로 디버깅 모드로 해도 괜찮다. 실제 서비스에서는 하면 안된다.