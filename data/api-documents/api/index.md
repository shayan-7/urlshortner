

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

`200 OK`

### Response Headers:

```
Content-Type: text/html; charset=utf-8
Content-Length: 351
```
### Response Body:

```json
<html>
<head><title>Url shortener</title></head>
<body>
        <div style="background-color:DodgerBlue;color:white;padding:20px;">
        <form method="POST" action="/">
        <strong>Iuput url:</strong>
            <input type="text" name="url" />
            <input type="submit" value="Submit" />
        </form>
        </div>
</body>
</html>
```


