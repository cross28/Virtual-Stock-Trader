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

Once this is done, you can save the program and move to the terminal. You can play the game by running the Game.py script, or it can be turned into an executable with the pyinstaller library.

Open the terminal and type:
```
pip3 install pyinstaller
```

Once that installs, in the terminal, go to the directory of the scripts. In their you'll want to type:
```
pyinstaller --onefile Game.py
```

After the script is done, you will see a new file and folder.

Build, dist, and Game.spec:

![alt text](/images/folder.png)

The main item to focus on is the /dist folder. Go into the /dist folder and the game executable will be in it.

![alt text](/images/dist.png)

Here you will want to move the executable back one directory where all the python scripts are.

![alt text](/images/moved.png)

And then the program is all setup. A shortcut to the executable in the file can be made to put on the desktop.
