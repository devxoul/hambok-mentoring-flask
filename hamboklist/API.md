# Hamboklist REST API v1.0 Document

<br />




## 1. Concepts

###### HTTP STATUS

| Status | Description |
|---|---|
| 200 | OK |
| 201 | Created, Done |
| 400 | Bad parameter |
| 403 | Not authorized |
| 404 | Not found |
| 405 | Unexpected method |	
	
<br /><br />








## 2. Auth

### `POST` /login

###### Description

로그인


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/login`


###### Request

| Name | Required | Description |
|---|---|---|
| **email** | *Required* |  |
| **password** | *Required* | SHA-1 |


###### HTTP Status

201


###### Sample JSON Response

```
{
    "email": "ceo@joyfl.net",
    "id": 1,
    "name": null
}
```


<br /><br />






### `GET` /logout

###### Description

로그아웃


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/logout`



###### HTTP Status

200


###### Sample JSON Response

```
{}
```



<br /><br />





## 3. User

### `POST` /user

###### Description

회원가입


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/user`


###### HTTP Status

201


###### Sample JSON Response

```
{
    "email": "ceo@joyfl.net",
    "id": 1,
    "name": null
}
```


<br /><br />






### `GET` /user

###### Description

유저정보 얻기


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/user`


###### HTTP Status

200


###### Sample JSON Response

```
{
    "email": "ceo@joyfl.net",
    "id": 1,
    "name": null
}
```


<br /><br />






### `PUT` /user

###### Description

사용자 정보 수정


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/user`


###### Request

| Name | Required | Description |
|---|---|---|
| **email** | *Optional* |  |
| **password** | *Optional* | SHA-1 |
| **name** | *Optional* |  |


###### HTTP Status

200


###### Sample JSON Response

```
{
    "email": "ceo@joyfl.net",
    "id": 1,
    "name": null
}
```


<br /><br />







### `DELETE` /user

###### Description

사용자 삭제


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/user`


###### HTTP Status

200


###### Sample JSON Response

```
{}
```



<br /><br />






## 4. List

### `GET` /lists

###### Description

사용자의 리스트


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/lists`


###### HTTP Status

200


###### Sample JSON Response

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





<br /><br />




### `GET` /list/{id}

###### Description

리스트


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/list/{id}`


###### HTTP Status

200


###### Sample JSON Response

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





<br /><br />






### `POST` /list

###### Description

리스트 만들기


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/list`


###### Request

| Name | Required | Description |
|---|---|---|
| **name** | *Required* |  |


###### Sample JSON Response

```
{
    "tasks": [],
    "id": 3,
    "name": ""
}
```



<br /><br />





### `PUT` /list/{id}

###### Description

리스트 정보 수정하기


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/list/{id}`


###### Request

| Name | Required | Description |
|---|---|---|
| **name** | *Required* |  |


###### HTTP Status

200


###### Sample JSON Response

```
{
    "tasks": [],
    "id": 3,
    "name": ""
}
```



<br /><br />






### `DELETE` /list/{id}

###### Description

리스트 삭제하기


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/list/{id}`



###### HTTP Status

200


###### Sample JSON Response

```
{}
```


<br /><br />





## 5. Task

### `POST` /list/{id}/task

###### Description

리스트에 태스크 추가하기


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/list/{id}/task`


###### Request

| Name | Required | Description |
|---|---|---|
| **title** | *Required* |  |
| **description** | *Optional* |  |


###### HTTP Status

201


###### Sample JSON Response

```
{
    "description": "",
    "id": 4,
    "complete": false,
    "title": ""
}
```



<br /><br />





### `PUT` /task/{id}

###### Description

태스크 정보 수정하기


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/task/{id}`


###### Request

| Name | Required | Description |
|---|---|---|
| **title** | *Optional* |  |
| **description** | *Optional* |  |
| **complete** | *Optional* | 0 or 1 |
| **list_id** | *Optional* |  |



###### HTTP Status

200


###### Sample JSON Response

```
{
    "description": "",
    "id": 4,
    "complete": false,
    "title": ""
}
```


<br /><br />






### `DELETE` /task/{id}

###### Description

태스크 삭제하기


###### URL Structure

`http://smarteen.xoul.kr/xoul/hamboklist/api/task/{id}`



###### Sample JSON Response

```
{}
```