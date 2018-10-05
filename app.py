import os, json

from flask import Flask, g, render_template, redirect, url_for
from flask_restful import Resource, Api

from graph_db import driver

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_db():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)

