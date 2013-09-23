# Hamboklist (햄볶리스트)

## 제 1장. 기획

### 1.1 컨셉

햄볶리스트는 기본적인 기능으로만 이루어진 To-Do List 관리 애플리케이션이다. 이 애플리케이션을 사용해서 할 일 목록을 관리하면 인생이 조금 더 햄볶해질 것이다.

<br />

### 1.2 기능 설계

#### 1.2.1 로그인 시스템

햄볶리스트는 로그인 시스템을 갖추고 있다. 사용자별로 자신의 할 일 목록을 서버에 저장시켜놓고, REST API를 통해 언제든지 클라이언트에서 할 일 목록을 가져오고, 추가하고, 변경할 수 있다.

* 로그인
* 로그아웃
* 회원가입
* 회원정보 변경
* 회원탈퇴


#### 1.2.2 목록(List)별 할 일 관리

사용자는 할 일을 목록별로 관리할 수 있다. 당연한 소리겠지만 자신의 목록은 자신만 열람이 가능하다.

* 내 목록 열람
* 목록 추가
* 목록 변경
* 목록 삭제


#### 1.2.3 할 일(Task)

사용자는 할 일을 만들고 삭제하고 수정할 수 있다. 완료한 작업은 따로 표시할 수 있다.

* 리스트별 태스크 열람
* 리스트에 태스크 추가
* 태스크 변경
* 태스크 삭제

<br />

### 1.3 Model 설계

#### 1.3.1 User

| 속성 | 타입 | 설명 |
|---|---|---|
| **id** | Integer | 각 레코드들의 고유 식별자 |
| **name** | String[40] | 사용자 이름 |
| **email** | String[40] | 사용자 이메일 |
| **password** | String[160] | 비밀번호, SHA-1 알고리즘 사용 |


#### 1.3.2 List

| 속성 | 타입 | 설명 |
|---|---|---|
| **id** | Integer | 각 목록을 구분짓는 고유 식별자 |
| **name** | String[40] | 목록 이름 |
| **user_id** | Integer | 이 목록을 가진 사용자의 id |

	
#### 1.3.3 Task

| 속성 | 타입 | 설명 |
|---|---|---|
| **id** | Integer | 각 태스크들의 고유 식별자 |
| **title** | String[40] | 할 일 제목 |
| **description** | Text | 할 일 내용 |
| **complete** | Boolean | 완료 여부 |
| **list_id** | Integer | 이 할 일을 가진 목록 id |
| **user_id** | Integer | 이 할 일을 가진 사용자의 id |

<br />

### 1.4 API 설계

API 설계는 1.2에서 설계한 기능을 실제로 사용할 수 있는 API로 바꿔주는 작업이다. API를 설계할 때에는 1.3에서 설계한 모델을 중심으로, 각 모델에 필요한 기능을 적절하게 설계하면 된다. 우리는 여기서 REST 형식에 맞게 API를 설계할 것이다.

<br />

#### 1.4.1 사전지식

##### 1.4.1.1 HTTP (Hyper Text Transfer Protocol)

HTTP를 단어 그대로 풀어보자면 '하이퍼텍스트(Hyper Text)를 전송할 때 사용되는 통신규약'이다. 서버와 클라이언트가 통신할 때 서로 어떻게 통신할지를 미리 정해둔 것이다.

HTTP는 크게 클라이언트가 서버로 보내는 요청(Request)과, 요청에 대해서 서버가 클라이언트로 보내는 응답(Response)으로 나뉜다. 각 요청과 응답에는 헤더(Header)와 바디(Body)가 있는데, 헤더 부분에는 어떻게 통신할 것인지에 대해서 정의되어있고, 바디 부분에는 실제 데이터가 담겨있다.

우리가 인터넷 브라우저에 http://google.com 을 입력해서 이동 버튼을 누르면, 브라우저는 google.com 이라는 곳으로 HTTP 요청을 만들어서 보낸다. 그럼 서버에서는 우리가 보낸 요청을 읽어들이고, 요청에 맞게 처리하여 응답을 보낸다. 이 응답의 바디에 실제 웹사이트의 HTML 데이터가 들어있고, 웹브라우저가 이를 그래픽으로 만들어 보여주게 된다.

HTTP는 너무 방대한 내용이라 설명을 읽고 이해하기보다는, 반복적으로 사용해보며 몸으로 받아들이는 것이 좋다.

<br />

##### 1.4.1.2 REST (Representational State Transfer)

'REST'라는 말을 많이 볼 수 있을텐데, REST는 소프트웨어 아키텍처의 한 형식이다. 서버와 클라이언트가 적절하게 통신할 수 있도록 정형화된 API 설계라고 생각하면 쉽다. REST에서는 '리소스(Resource)'와 '인터페이스(Interface)', 그리고 'Representation'이라는 개념이 특히 중요한데, 리소스는 우리가 1.3에서 설계한 모델의 실제 데이터라고 생각하면 되고, 인터페이스는 우리가 이번에 설계할 API라고 생각하면 된다.

우리는 잘 정의된 인터페이스를 통해 리소스에 접근할 수 있다. 하지만 우리는 데이터베이스 자체를 클라이언트로 전송하지 않고, JSON이나 XML과 같은, 리소스와는 개념적으로 분리된 Representation을 통해 클라이언트로 전송한다.

위키피디아를 참고하면 더 자세한 내용을 볼 수 있다: http://ko.wikipedia.org/wiki/REST

<br />

##### 1.4.1.3 HTTP Method

HTTP 요청을 보낼 때에는 몇 가지 방법을 통해 보낼 수 있다. HTTP에는 여러가지 메소드가 있지만 가장 많이 사용되는 것은 GET, POST, PUT, DELETE 4가지이다. 각각은 주로 다음과 같은 기능을 할 때 사용된다.

<br />
* GET : 데이터를 가져올 때 사용된다.
* POST : 새로운 데이터를 생성할 때 사용된다.
* PUT : 기존 데이터를 수정할 때 사용된다.
* DELETE : 데이터를 삭제할 때 사용된다.

HTTP Method는 1.4.1.4에서 배울 URL Pattern과 함께 RESTful API를 만드는데 매우 중요한 역할을 한다.

<br />

##### 1.4.1.4 URL Pattern

URL Pattern은 특정한 개념은 아니지만, RESTful API에서 권장하는 설계에 대해서 알아보자.

* 각 URL은 오브젝트를 가리킨다. 예를 들어, 리스트를 가리키는 URL은  `/list`가 될 것이다.
* 상태를 변경하기 위해서는 HTTP Method를 통해 행동을 지시한다. 예를들어, 리스트를 추가하는 요청은 `POST /list`가 된다.
* 특정 오브젝트를 가리키기 위해서는 id를 사용하는데, 오브젝트 뒤에 슬래시('/')를 붙여 id를 지정한다. 예를 들어, 10번 리스트를 가리키는 URL은 `/list/10`이 될 것이다.
* 해당 오브젝트를 여러개 가져오기 위해서는 복수형 단어를 쓰면 된다. 리스트 전체를 가리키는 URL은 `/lists`가 된다.
* 슬래시('/')로 각 오브젝트의 하위 오브젝트에 접근할 수 있다. 태스크는 리스트에 속하므로, 10번 리스트의 할 일 목록을 가리키는 URL은 '/list/10/tasks'가 된다.
* Depth(깊이)를 최대한 줄인다. 10번 리스트의 3번 태스크에 접근하려면 '/list/10/task/3'을 쓸 수도 있지만, 각 Task는 모두 고유한 id를 가지고있기 때문에 `/task/3`을 통해서도 같은 데이터에 접근이 가능하다.
* `/list/10`에서와 같이 URL이 동적으로 변경되는 곳은 {}나 <>를 사용해서 표기를 하는 경우가 많다. `/list/{id}`와 같이 표기하면, 특정 id를 가진 리스트를 가리키는 URL이 된다.

<br />

#### 1.4.2 모델별 기능 정리

1.2에서 설계했던 기능을 1.3에서 설계한 모델에 맞게 정리해보자. 그리고, 1.4.1에서 알게된 지식을 이용해서 각 기능을 적절한 HTTP Method와 URL Pattern에 맞게 매칭해보자. 로그인과 로그아웃은 조금 특별한 기능이니 여기서는 생략하도록 하자.

* User
 * 로그인
 * 로그아웃
 * 회원가입 → `POST` /user
 * 회원정보 변경 → `PUT` /user/{id}
 * 회원탈퇴 → `DELETE` /user/{id}

* List
 * 내 목록 열람 → `GET` /lists
 * 목록 추가 → `POST` /list
 * 목록 변경 → `PUT` /list/{id}
 * 목록 삭제 → `DELETE` /list/{id}

* Task
 * 리스트별 태스크 열람 → `GET` /list/{id}/tasks
 * 리스트에 태스크 추가 → `POST` /list/{id}/task
 * 태스크 변경 → `PUT` /task/{id}
 * 태스크 삭제 → `DELETE` /task/{id}

<br />

#### 1.4.3 로그인과 로그아웃

로그인과 로그아웃은 조금 특별한 동작을 한다. 로그인을 하면 '세션(Session)'이라는 것을 만들고, 로그아웃을 하면 세션을 닫는다. 로그인이 필요한 기능은 세션이 열려있어야 사용이 가능하다. 세션은 서버에서 관리되는데, 세션이 열리면 클라이언트에 고유한 키를 발급해주고, HTTP 통신을 할 때마다 이 고유키에 해당하는 세션이 열려있는지를 검사해서 로그인이 되어있는지를 확인할 수 있다.

로그인과 로그아웃은 `POST /login`, `POST /logout`으로 설계하는 경우가 많다.

<br />

#### 1.4.4 API 문서 작성

설계한 API를 가지고 문서를 작성해보자. 문서에는 URL 패턴과 HTTP Method로 각 API를 구분하고, 각 API별로 설명과 요청, 응답이 정의되어있어야 한다. 에러코드와 참고항목도 넣어야 하지만, 우리는 생략하도록 하자.

<br />

##### 1.4.4.1  `POST` /login

###### 설명

로그인

###### 요청

| 이름 | 옵션 | 설명 |
|---|---|---|
| **email** | *필수* |  |
| **password** | *필수* | SHA-1 |

###### 응답

로그인한 사용자 정보를 리턴한다.

```
{
    "email": "devxoul@gmail.com",
    "id": 1,
    "name": "Su Yeol Jeon"
}
```

<br />

##### 1.4.4.2 `GET` /logout

###### 설명

로그아웃

###### 응답

```
{}
```

<br />

##### 1.4.4.3 `POST` /user

###### 설명

사용자 생성 (회원가입)

###### 응답

생성된 사용자 정보를 보여준다.

```
{
    "email": "devxoul@gmail.com",
    "id": 1,
    "name": "Su Yeol Jeon"
}
```

<br />

##### 1.4.4.4 `GET` /user

###### Description

유저정보 얻기

###### 응답

```
{
    "email": "devxoul@gmail.com",
    "id": 1,
    "name": "Su Yeol Jeon"
}
```

<br />

##### 1.4.4.5 `PUT` /user

###### Description

사용자 정보 수정

###### 요청

| 이름 | 옵션 | 설명 |
|---|---|---|
| **email** | *선택* |  |
| **password** | *선택* | SHA-1 |
| **name** | *선택* |  |

###### 응답

수정 후의 사용자 정보를 리턴한다.

```
{
    "email": "devxoul@gmail.com",
    "id": 1,
    "name": "Su Yeol Jeon"
}
```
<br />

##### 1.4.4.6 `DELETE` /user

###### Description

사용자 삭제

###### 응답

```
{}
```

<br />

#####1.4.4.7  `GET` /lists

###### Description

사용자의 리스트

###### 응답

```
{
    "lists": [
        {
            "tasks": [],
            "id": 1,
            "name": ""
        },
        {
            "tasks": [
                {
                    "description": null,
                    "id": 3,
                    "complete": false,
                    "title": ""
                }
            ],
            "id": 2,
            "name": ""
        },
        {
            "tasks": [
                {
                    "description": null,
                    "id": 1,
                    "complete": true,
                    "title": ""
                },
                {
                    "description": "",
                    "id": 2,
                    "complete": false,
                    "title": ""
                }
            ],
            "id": 3,
            "name": ""
        }
    ]
}
```

<br />

##### 1.4.4.8 `GET` /list/{id}

###### Description

리스트 하나

###### 응답

```
{
    "tasks": [
        {
            "description": null,
            "id": ,
            "complete": ,
            "title": ""
        },
        {
            "description": "",
            "id": ,
            "complete": ,
            "title": ""
        }
    ],
    "id": ,
    "name": ""
}
```

<br />

##### 1.4.4.9 `POST` /list

###### Description

리스트 만들기

###### 요청

| 이름 | 옵션 | 설명 |
|---|---|---|
| **name** | *필수* |  |


###### 응답

```
{
    "tasks": [],
    "id": 3,
    "name": ""
}
```

<br />

##### 1.4.4.10 `PUT` /list/{id}

###### Description

리스트 정보 수정하기

###### 요청

| 이름 | 옵션 | 설명 |
|---|---|---|
| **name** | *필수* |  |

###### 응답

정보가 수정된 리스트 정보를 리턴한다.

```
{
    "tasks": [],
    "id": 3,
    "name": ""
}
```

<br />

##### 1.4.4.11 `DELETE` /list/{id}

###### Description

리스트 삭제하기

###### 응답

```
{}
```

<br />

##### 1.4.4.12 `POST` /list/{id}/task

###### Description

리스트에 태스크 추가하기

###### 요청

| 이름 | 옵션 | 설명 |
|---|---|---|
| **title** | *필수* |  |
| **description** | *선택* |  |

###### 응답

추가된 태스크 정보를 리턴한다.

```
{
    "description": "",
    "id": 4,
    "complete": false,
    "title": ""
}
```

<br />

##### 1.4.4.13 `PUT` /task/{id}

###### Description

태스크 정보 수정하기

###### 요청

| 이름 | 옵션 | 설명 |
|---|---|---|
| **title** | *선택* |  |
| **description** | *선택* |  |
| **complete** | *선택* | 0 or 1 |
| **list_id** | *선택* |  |

###### 응답

정보가 수정된 태스크 정보를 리턴한다.

```
{
    "description": "",
    "id": 4,
    "complete": false,
    "title": ""
}
```

<br />

##### 1.4.4.14 `DELETE` /task/{id}

###### Description

태스크 삭제하기

###### 응답

```
{}
```

<br />

---

## 제 2장. 개발

### 2.1 Flask 세팅

#### 2.1.1 가상환경(virtualenv) 세팅


앞으로 우리가 작업을 할 폴더를 만든다. 이 문서에서는 'hamboklist'라는 이름을 사용하기로 한다. hamboklist 디렉토리에서 `virtualenv venv` 명령어를 입력해서 `venv` 폴더를 가상환경 설정폴더로 지정한다.

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

<br />

#### 2.1.2 Flask 설치하기

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

Flask를 설치하면 Jinja2, Werkzeug 등 다른 패키지들도 함께 설치되는데, 이는 Flask가 해당 패키지들을 기본적으로 사용하고 있기 때문이다. [Jinja2](http://jinja.pocoo.org/docs/)는 템플릿 엔진이고, [Werkzeug](http://werkzeug.pocoo.org/docs/)는 WSGI 툴킷이다.

<br />


### 2.2 Flask 프로젝트 구조 설계

본격적으로 개발에 들어가기 전에, 프로젝트의 구조를 먼저 잡아놓고 시작하자. Flask는 Microframework라는 소개문구에 걸맞게 매우 작으면서도 확장가능한 구조를 가지고 있다. (심지어 하나의 파일로도 애플리케이션을 만들 수 있다.)

매우 유연한 구조를 가진 만큼 프로젝트 구조를 설계하는데 있어서도 정해진 답이 없다. 따라서 여러 구조를 시도해보며 단점을 보완해나가며 프로젝트에 맞게 자신만의 구조를 잡아나가는 것이 좋다.

프로젝트 구조를 설계할 때, 아래 내용을 신경써서 설계하면 도움이 된다.
* 설정파일 분리하기
* 비슷한 기능을 하는 파일들은 패키지(폴더)로 분리하기

> **파이썬 패키지**
>
> 패키지는 쉽게 말하면 파이썬 모듈을 디렉토리로 구조화한 것이다. 2.1.2에서 설치한 Flask도 하나의 패키지이다. 디렉토리를 패키지로 만드려면 그 디렉토리 안에 `__init__.py`라는 이름의 파이썬 파일을 하나 만들면 된다. (빈 파일이어도 괜찮다. 특별한 일이 없으면 빈 파일인 경우가 많다.) 디렉토리 이름이 곧 패키지 이름이 된다. 이렇게 만든 패키지는 파이썬 코드를 작성할 때 'import 패키지' 또는 'from 패키지 import 모듈'과 같이 사용할 수 있다.

지금 여러분의 hamboklist 디렉토리에는 가상환경 파일들이 담긴 venv라는 폴더밖에 없을 것이다. 여기에 우리가 실제로 애플리케이션 코드를 작성할 패키지를 하나 만들자. 이름은 여러분 자유지만, 이곳에서는 hamboklist라는 이름의 파이썬 패키지를 만들 것이다.

```
(venv)$ mkdir hamboklist
(venv)$ touch hamboklist/__init__.py
```

디렉토리를 만들고, 그 디렉토리를 패키지로 만들기 위해 touch 명령어로 \_\_init__.py라는 빈 파일을 생성했다. 같은 방법으로 `app.py`, `database.py`, `model.py`를 `hamboklist` 패키지 안에 만들자. 그리고 `views` 패키지를 만들고 `api.py`를 그 안에 넣어주자.

여기까지 했으면 디렉토리가 아래와 같은 구조로 되어있을 것이다. (venv 내부는 생략)

```
hamboklist
|-- hamboklist
|	|-- __init__.py
|	|-- app.py
|	|-- database.py
|	|-- model.py
|	`-- views
|		|-- __init__.py
|		`-- api.py
`-- venv
```

이제, 각 파일들을 하나하나 열어서 개발해보자.

<br />

### 2.3 app.py




### 2.4 database.py


### 2.5 model.py


### 2.6 api.py



<br />

---

## 제 3장. 서비스 구동하기