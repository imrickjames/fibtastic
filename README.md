# fibtastic

# To get up and running:
    git clone https://github.com/imrickjames/fibtastic.git
    cd fibtastic
    mkvirtualenv fibtastic (workon fibtastic if necessary)
    pip install -r requirements/dev.txt
    python manage.py create_db
    python manage.py runserver
    python manage.py drop_db when done

# API Interactions:

## create
    curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d ' { "n": 10 } ' http://localhost:5000/fibtastic
    * Hostname was NOT found in DNS cache
    *   Trying 127.0.0.1...
    * Connected to localhost (127.0.0.1) port 5000 (#0)
    > POST /fibtastic HTTP/1.1
    > User-Agent: curl/7.37.1
    > Host: localhost:5000
    > Accept: application/json
    > Content-type: application/json
    > Content-Length: 13
    >
    * upload completely sent off: 13 out of 13 bytes
    * HTTP 1.0, assume close after body
    < HTTP/1.0 201 CREATED
    < Content-Type: application/json
    < Content-Length: 172
    < Server: Werkzeug/0.10.1 Python/2.7.6
    < Date: Mon, 16 Mar 2015 07:17:29 GMT
    <
    {
      "id": 1,
      "sequence": [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55
      ],
      "url": "http://localhost:5000/fibtastic/1"
    * Closing connection 0
    }

## Get specific
    curl -v -H "Accept: application/json" -H "Content-type: application/json" http://localhost:5000/fibtastic/1
    * Hostname was NOT found in DNS cache
    *   Trying 127.0.0.1...
    * Connected to localhost (127.0.0.1) port 5000 (#0)
    > GET /fibtastic/1 HTTP/1.1
    > User-Agent: curl/7.37.1
    > Host: localhost:5000
    > Accept: application/json
    > Content-type: application/json
    >
    * HTTP 1.0, assume close after body
    < HTTP/1.0 200 OK
    < Content-Type: application/json
    < Content-Length: 125
    < Server: Werkzeug/0.10.1 Python/2.7.6
    < Date: Mon, 16 Mar 2015 07:18:05 GMT
    <
    {
      "id": 1,
      "sequence": [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55
      ]
    * Closing connection 0
    }

## delete
    curl -v -H "Accept: application/json" -H "Content-type: application/json" -X DELETE http://localhost:5000/fibtastic/1
    * Hostname was NOT found in DNS cache
    *   Trying 127.0.0.1...
    * Connected to localhost (127.0.0.1) port 5000 (#0)
    > DELETE /fibtastic/3 HTTP/1.1
    > User-Agent: curl/7.37.1
    > Host: localhost:5000
    > Accept: application/json
    > Content-type: application/json
    >
    * HTTP 1.0, assume close after body
    < HTTP/1.0 200 OK
    < Content-Type: application/json
    < Content-Length: 47
    < Server: Werkzeug/0.10.1 Python/2.7.6
    < Date: Mon, 16 Mar 2015 07:22:03 GMT
    <
    {
      "response": "Fib 1 successfully deleted."
    * Closing connection 0
    }

## Logging example (/var/tmp/app.fibtastic.log)
    2015-03-16 02:25:18,803 INFO    : addr: 127.0.0.1 | msg: Created fib id:6 | rcode: 204
    2015-03-16 02:25:20,866 INFO    : addr: 127.0.0.1 | msg: Created fib id:7 | rcode: 204
    2015-03-16 02:25:21,592 INFO    : addr: 127.0.0.1 | msg: Created fib id:8 | rcode: 204
    2015-03-16 02:25:22,240 INFO    : addr: 127.0.0.1 | msg: Created fib id:9 | rcode: 204
    2015-03-16 02:25:22,848 INFO    : addr: 127.0.0.1 | msg: Created fib id:10 | rcode: 204
    2015-03-16 02:25:38,616 INFO    : addr: 127.0.0.1 | msg: Deleted fib id:10 | rcode: 200
    2015-03-16 02:25:42,632 INFO    : addr: 127.0.0.1 | msg: Deleted fib id:9 | rcode: 200
    2015-03-16 02:25:51,363 ERROR   : addr: 127.0.0.1 | err: parameter n must be a non-negative integer | rcode: 400
    2015-03-16 02:26:06,234 ERROR   : addr: 127.0.0.1 | err: Parameter n must be passed | rcode: 400




