# Hamboklist (햄볶리스트)

## 제 1장. 기획

### 1.1 컨셉

햄볶리스트는 기본적인 기능으로만 이루어진 To-Do List 관리 애플리케이션이다. 이 애플리케이션을 사용해서 할 일 목록을 관리하면 인생이 조금 더 햄볶해질 것이다.

<br />

### 1.2 기능 설계

#### 1.2.1 로그인 시스템

햄볶리스트는 로그인 시스템을 갖추고 있다. 사용자별로 자신의 할 일 목록을 서버에 저장시켜놓고, REST API를 통해 언제든지 클라이언트에서 할 일 목록을 가져오고, 추가하고, 변경할 수 있다.

* 로그인
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
* 태스크 추가
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

> **REST (Representational State Transfer)**
>
> 'REST'라는 말을 많이 볼 수 있을텐데, REST는 소프트웨어 아키텍처의 한 형식이다. 서버와 클라이언트가 적절하게 통신할 수 있도록 정형화된 API 설계라고 생각하면 쉽다. REST에서는 '리소스(Resource)'와 '인터페이스(Interface)', 그리고 'Representation'이라는 개념이 특히 중요한데, 리소스는 우리가 1.3에서 설계한 모델의 실제 데이터라고 생각하면 되고, 인터페이스는 우리가 이번에 설계할 API라고 생각하면 된다. 우리는 잘 정의된 인터페이스를 통해 리소스에 접근할 수 있다. 하지만 우리는 데이터베이스 자체를 클라이언트로 전송하지 않고, JSON이나 XML과 같은, 리소스와 개념적으로 분리된 Representation을 통해 클라이언트로 전송한다. 위키피디아를 참고하면 더 자세한 내용을 볼 수 있다: http://ko.wikipedia.org/wiki/REST

#### 1.4.1 User

##### 1.4.1.1  `POST` /login

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

##### 1.4.1.2 `GET` /logout

###### 설명

로그아웃

###### 응답

```
{}
```

<br />

##### 1.4.1.3 `POST` /user

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

##### 1.4.1.4 `GET` /user

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

##### 1.4.1.5 `PUT` /user

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

##### 1.4.1.6 `DELETE` /user

###### Description

사용자 삭제

###### 응답

```
{}
```

<br />

#### 1.4.2 List

#####1.4.2.1  `GET` /lists

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

##### 1.4.2.2 `GET` /list/{id}

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

##### 1.4.2.3 `POST` /list

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

##### 1.4.2.4 `PUT` /list/{id}

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

##### 1.4.2.5 `DELETE` /list/{id}

###### Description

리스트 삭제하기

###### 응답

```
{}
```

<br />

#### 1.4.3 Task

##### 1.4.3.1 `POST` /list/{id}/task

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

##### 1.4.3.2 `PUT` /task/{id}

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

##### 1.4.3.3 `DELETE` /task/{id}

###### Description

태스크 삭제하기

###### 응답

```
{}
```

<br />

---

# 제 2장. 개발

## 2.1 Flask 설치


## 2.2 Flask 프로젝트 구조 설계


## 2.3 model.py


## 2.4 api.py



<br />

---

# 제 3장. 서비스 구동하기