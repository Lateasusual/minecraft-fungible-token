from flask import Flask, request, Response, jsonify, redirect
import os
from threading import Thread
import sqlite3 as sq


app = Flask(__name__)

@app.route('/mft/place_block', methods=['GET', 'POST'])
def respond():
    data = request.form.get("message", None)

    print(f"message received: {data}")

    con = sq.connect("messages.db")
    with con:
        con.execute("INSERT INTO MESSAGES (message) values (?)", [str(data)])

    return redirect("block_placed.html")
