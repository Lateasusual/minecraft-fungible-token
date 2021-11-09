# minecraft-fungible-token
Stupid shitpost

In order to use this you'll need to setup your web server to run the flask app in the .backend folder, and to redirect traffic from /mft/place_block to there.
You'll also need to create the SQL database to store the messages in - the python code below will do that, run it in the .backend folder also.

```py
import sqlite3 as sq

con = sq.connect("messages.db")
con.execute("CREATE TABLE MESSAGES (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, message TEXT);")
```

The images are all either ingame screenshots or from google images, none of them are mine.
