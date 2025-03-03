# Server

## Sequence Plan

* periodically pull emails
* check for new emails
* parse email subject
* serve message to web API
  * JSON

## Protokoll Specification

* timestamp according to RFC3339

```json
[
    {
        "id": 0,
        "timestamp": "1970-01-01T00:00:00-00:00",
        "message": "projector problem in room 42"
    }
]
```
