from flask import Flask, request, redirect
import random

app = Flask(__name__)

nextID = 4
Topics = [  # 아래 리스트는 데이터 베이스로 제어하는 것을 권장한다.
    {'id' : 1, 'title': 'HTML', 'body' : 'html is ...'},
    {'id' : 2, 'title': 'CSS', 'body' : 'CSS is ...'},
    {'id' : 3, 'title': 'JavaScript', 'body' : 'JavaScript is ...'}
]

def Template(contents, content, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
            <li><form action="/delete/{id}/" method="POST"><input type="submit" value="delete"></form>
        '''
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
        <ul><li><a href="/create/">crate</a></li></ul>
        {contextUI}
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
    return Template(getContents(), f'<h2>{title}</h2>{body}', id)

# request.method를 통해 GET, POST를 구분한다. 
@app.route('/create/', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        # 데이터를 url을 통해 전송하는 방식을 get 방식이라고 부른다. get은 사용자(클라이언트)입장에서 가져오는 것이다. 
        # 데이터를 수정할 때는 method="POST"을 통해 수정한다. 
        # 참고로 method는 method="GET" 또는 method="POST"가 될 수 있다. 
        content = '''
            <form action="/create/" method="POST"> 
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return Template(getContents(), content)
    elif request.method == "POST":
        global nextID  # 전역변수로 바꾸는 방법
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextID, 'title':title, 'body':body}
        Topics.append(newTopic)
        url = '/read/'+str(nextID)+'/'
        nextID += 1  # 여기서 nextID에 1을 더하기 위해 전역 변수를 사용한다. 
        return redirect(url)




@app.route('/update/<int:id>/', methods=["GET", "POST"])
def update(id):
    if request.method == "GET":
            title = ''
            body = ''
            for Topic in Topics:
                if id == Topic['id']:  # 조회하기
                    title = Topic['title']
                    body = Topic['body']
                break
            content = f'''
                <form action="/update/{id}/" method="POST"> 
                    <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                    <p><textarea name="body" placeholder="body">{body}</textarea></p>
                    <p><input type="submit" value="update"></p>
                </form>
            '''
            return Template(getContents(), content)
    elif request.method == "POST":
        title = request.form['title']
        body = request.form['body']
        for Topic in Topics:
            if id == Topic[id]:
                Topic['title'] = title
                Topic['body'] = body
                break
        url = '/read/'+str(id)+'/'
        return redirect(url)

# 삭제 기능은 POST를 통해 기능을 구현한다. a태그 링크를 제공하면 곤란하다.
@app.route('/delete/<int:id>/', methods=["POST"])
def delete(id):
    for Topic in Topics:
        if id == Topic[id]:
            Topics.remove(Topic)
            break
    return redirect('/')  # 삭제를 하면 홈으로 돌아감

if __name__ == "__main__":
    app.run(port=3000, debug=True)  # 개발 중에는 debug=True로 디버깅 모드로 해도 괜찮다. 실제 서비스에서는 사용하면 곤란하다.