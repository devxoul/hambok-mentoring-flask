# 수열이의 햄볶한 멘토링 - Flask

## 1. Flask 기본 세팅

### 1-1. 가상환경(virtualenv) 세팅

작업중인 디렉토리에서 `virtualenv venv` 명령어를 입력해서 `venv` 폴더를 가상환경 설정폴더로 지정한다.

```
$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools............done.
Installing pip...............done.
```

가상환경 세팅이 완료되면 `venv` 폴더에 가상환경 관련 파일들이 담겨지게 된다.

현재 디렉토리의 가상환경으로 활성화시키려면 `. venv/bin/activate` 명령어를 입력하면 된다.

```
$ . venv/bin/activate
(venv)$
```

가상환경이 활성화되어있으면 쉘에 `(venv)`가 표시된다. 가상환경을 비활성화시키려면 `deactivate` 명령어를 입력하면 된다.

```
(venv)$ deactivate
$
```



### 1-2. Flask 설치하기

Flask는 `pip` 명령어로 쉽게 설치할 수 있다. 가상환경이 활성화된 상태에서 `pip` 명령어를 통해 설치한 패키지들은 가상환경 세팅폴더로 지정된 `./venv/lib/python2.7/site-packages/` 디렉토리에 저장된다.

```
(venv)$ pip install flask
Downloading/unpacking flask
  Downloading Flask-0.10.1.tar.gz (544kB): 544kB downloaded
  Running setup.py egg_info for package flask
.
.
.
Successfully installed flask Werkzeug Jinja2 itsdangerous markupsafe
Cleaning up...
```

Flask가 제대로 설치되었는지 여부는 `pip list` 명령어를 통해 확인할 수 있다.

```
(venv)$ pip list
Flask (0.10.1)
itsdangerous (0.23)
Jinja2 (2.7.1)
MarkupSafe (0.18)
Werkzeug (0.9.4)
wsgiref (0.1.2)
```

Flask를 설치하면 Jinja2, Werkzeug 등 다른 패키지들도 함께 설치되는데, 이는 Flask가 해당 패키지들을 기본적으로 사용하고 있기 때문이다. [Jinja2][1]는 템플릿 엔진이고, [Werkzeug][2]는 WSGI 툴킷이다.



### 1-3. Hello, World! 출력하기

가장 기본적인 예제를 만들어보자. 이 예제는 [Flask 공식 웹사이트](http://flask.pocoo.org/)의 메인에도 있는 예제이다.

작업환경의 루트폴더에 hello.py라는 파일을 만들어보자. 이 파일의 이름이 여러분이 만드는 Flask 애플리케이션의 이름이 될 것이다. hello.py에는 아래의 내용을 입력하면 된다.

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run()
```

저장 후, 해당 파일을 python으로 실행해보자.

```
(venv)$ python hello.py
 * Running on http://127.0.0.1:5000/
```

Flask 웹서버가 로컬호스트(127.0.0.1)의 5000번 포트에서 실행되고 있다는 말이 나온다. 인터넷 브라우저를 켜서 주소창에 <http://127.0.0.1:5000>를 입력해서 들어가면 'Hello, World!'라는 텍스트가 보일 것이다. 실행중인 애플리케이션을 종료하려면 `Ctrl`키와 `C` 키를 함께 누르면 된다.


#### Host와 Port 직접 설정하기

host의 기본값은 '127.0.0.1'이고, port의 기본값은 5000이다. 만약 로컬환경이 아니라면, `app.run()` 함수의 인자로 host와 port를 직접 넣어주면 된다.

```
app.run(host='0.0.0.0', port=8080)
```


#### Debug Mode로 Flask 실행하기

`app.run()` 함수에 `debug=True` 옵션을 주면 디버그모드로 Flask를 실행할 수 있다. 디버그모드로 실행할 경우 메모리를 많이 먹게 되고 성능이 저하되므로 런칭시에는 Debug 옵션을 빼주도록 하자.



---



## 2. Flask 익히기

### 2-1. Route

Flask에서는 매우 직관적인 URL Routing을 지원한다. 첫 번째 Hello World 예제에서도 볼 수 있듯, `@app.route` 데코레이터(Decorator)로 함수를 지정하면, 그 함수에서 리턴한 결과가 실제로 클라이언트로 전송된다.

그럼, 작성한 코드를 아래와 같이 변경해보자.

```
@app.route('/')
def index():
	return 'It Works!'
	
@app.route('/hello')
def hello():
	return 'Hello, World!'
```

그리고, 인터넷 브라우저에서 <http://127.0.0.1:5000>과 <http://127.0.0.1:5000/hello>에 접속해보자. 각각 'It Works!'와 'Hello, World!'가 보이는 것을 확인할 수 있다.

이번에는 동적 URL을 다루기 위해 아래의 코드를 추가시켜보자.

```
@app.route('/user/<username>')
def get_user(username):
	return 'User %s' % username
```

인터넷 브라우저에서 <http://127.0.0.1:5000/user/xoul>로 접속해보자.'User xoul'이라는 결과를 볼 수 있다. URL을 지정해줄 때 '<'와 '>' 사이에 있는 변수가 함수의 인자로 넘어오게 된다. 변수가 여러 개라면 여러 개의 함수 인자를 선언해주면 된다.

만약 변수가 정수형이라면, `int:`를 추가시켜주면 된다.

```
@app.route('/post/<int:post_id>')
def get_post(post_id):
	return 'Post %d' % post_id
```

#### 한글 대응하기

만약 username에 영문이 아닌 유니코드를 입력하게되면 Python에러가 출력될 것이다. 유니코드를 처리하지 않아서 발생하는 에러인데, hello.py의 제일 윗줄에 `# -*- coding: utf-8 -*-`을 추가시켜주면 된다.



[1]: [http://jinja.pocoo.org/docs/] "Jinja2 Documentation"
[2]: [http://werkzeug.pocoo.org/docs/] "Werkzeug Documentation"