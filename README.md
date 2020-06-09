# python-stackoverflow-lld
## python StackOverflow Low Level Desing

run ```./home.py``` to execute the program

Here's a sample structure of app context hierarchy

```
[
    {
        "question": {
            "_id": "efe56755-4653-4f9a-b794-74a80daa6a8b",
            "_title": "ABC",
            "_body": "xyz",
            "_author": "rahul",
            "_createdAt": "2020-06-09 16:19:32.230932",
            "_editActivity": [],
            "_votes": {
                "_up": 1,
                "_down": 0
            },
            "_tags": [],
            "_flag": null,
            "_status": "OPEN",
            "_bounty": 0
        },
        "comments": [
            {
                "_id": "fcd29773-aa5e-4b9a-94f6-596cacde06ba",
                "_title": null,
                "_body": "my ABC Comment",
                "_author": "rahul",
                "_createdAt": "2020-06-09 16:19:32.231203",
                "_editActivity": [],
                "_votes": {
                    "_up": 0,
                    "_down": 0
                },
                "_tags": [],
                "_flag": null,
                "_post": "ABC"
            }
        ],
        "answers": {
            "7a2e818f-0a92-4e8f-b8c4-07eb79e82269": {
                "answer": {
                    "_id": "7a2e818f-0a92-4e8f-b8c4-07eb79e82269",
                    "_title": null,
                    "_body": "myABCanswer",
                    "_author": "rahul",
                    "_createdAt": "2020-06-09 16:19:32.231001",
                    "_editActivity": [],
                    "_votes": {
                        "_up": 0,
                        "_down": 1
                    },
                    "_tags": [],
                    "_flag": "irrelevant",
                    "_deleted": false,
                    "_question": "ABC",
                    "_bounty": 0
                },
                "comments": []
            }
        }
    },
    {
        "question": {
            "_id": "235a7365-bc78-4c38-b616-2501a0b06237",
            "_title": "ABC2",
            "_body": "xysdz",
            "_author": "rahul",
            "_createdAt": "2020-06-09 16:19:32.230975",
            "_editActivity": [],
            "_votes": {
                "_up": 0,
                "_down": 0
            },
            "_tags": [],
            "_flag": null,
            "_status": "OPEN",
            "_bounty": 0
        },
        "comments": [],
        "answers": {}
    }
]

```

