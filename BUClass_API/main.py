"""Main file for the BUClass_API."""

import sqlite3
from pathlib import Path

from flask import Flask, request

app = Flask(__name__)
parent_dir = Path(__file__).parent


@app.route('/')
def default():
    """Default page for the API."""

    welcome = '<h1>Welcome to BUClass_API!</h1>\
        Use: \
        <ul><li>/search?code= to search for a class.</li>\
        <li>/find?[query]= to filter classes by [query].</li></ul>'

    return welcome


@app.route('/search', methods=['GET'])
def search():
    """Search for a class by code."""

    req = request.args.get('code')
    con = sqlite3.connect(f'{parent_dir}/courses.db')
    cur = con.cursor()

    info = cur.execute(f'SELECT * \
                        FROM courses \
                        WHERE course = "{req}"')

    return [i for i in info.fetchall()[0]]


@app.route('/find', methods=['GET'])
def find():
    """Filter classes by prerequisite."""

    con = sqlite3.connect(f'{parent_dir}/courses.db')
    cur = con.cursor()
    query = {
        'prereq': '',
        'coreq': '',
        'credit': '',
        'hub': ''
    }

    base, count = 'SELECT course FROM courses WHERE', 0

    for section in query:
        req = request.args.get(section)

        if req and count > 0:
            base += ' AND'
        count += 1

        if req and section != 'credit':
            base += (f' {section} like "%{req}%"')

        elif req and section == 'credit':
            base += (f' {section} = "{req}"')

    info = cur.execute(base)
    clean_info = [i[0] for i in info.fetchall()]

    if clean_info:
        return f'{clean_info}'

    return 'No classes found.'


if __name__ == '__main__':
    # Local testing
    app.run(host='127.0.0.1', port=8080, debug=True)
