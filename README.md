# Virtual-Stock-Trader

**Version 1.0.0**

Created a virtual stock trading application in Python with 5 of tech giants using virtual money

---

## How to set up

First, to set up, you'll need your own api key for now. Head on over to [Alpha Vantage's Website](https://www.alphavantage.co/) and sign up for a free api key.

There are two methods to which you can insert your api key into the program:
* You can create a text document named 'secret.txt' and paste the api key directly into their
* Or you can go directly into the Game.py file and hard code it in.
Go to lines 40 and 41: 
```python
with open ('secret.txt', 'r') as r:
    api_key = r.read()
```

Remove this code, and put: 
```python
api_key = _your api key_
```
