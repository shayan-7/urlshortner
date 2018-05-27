

| Parameter | Value       |
| --------- | ----------- |
| Author    | TestEngine  |
| Version   | 0.1.0-planning.0 |
| Status    | Implemented |


index
=====
## GET `/`

Role: user



### Status:

`500 Internal server error`

### Response Headers:

```
Content-Type: text/plain; charset=utf-8
Content-Length: 632
```
### Response Body:

```json
Internal Server Error
Traceback (most recent call last):
  File "/home/mohammad/.virtualenvs/practice/lib/python3.6/site-packages/nanohttp/application.py", line 64, in __call__
    response_body = self.__root__(*remaining_paths)
  File "/home/mohammad/.virtualenvs/practice/lib/python3.6/site-packages/restfulpy/controllers.py", line 18, in __call__
    return super().__call__(*remaining_paths)
  File "/home/mohammad/.virtualenvs/practice/lib/python3.6/site-packages/nanohttp/controllers.py", line 81, in __call__
    handler, remaining_paths = self._find_handler(list(remaining_paths))
TypeError: 'method' object is not iterable
```


