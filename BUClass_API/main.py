from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def default():
    welcome = '<h1>Welcome to BUClass_API!</h1>\
        Use: \
        <ul><li>/search?code= to search for a class.</li>\
        <li>/filter?prereq= to filter classes by prerequisite.</li></ul>'

    return welcome


@app.route('/search', methods=['GET'])
def search():
    req = request.args.get('code')
    con = sqlite3.connect('BUClass_API/class_storage.db')
    cur = con.cursor()

    info = cur.execute(f'SELECT * \
                        FROM ClassData \
                        WHERE Name = "{req}"')

    clean_info = [i for i in info.fetchall()[0]]
    hub_credit = clean_info[-1].split("'")
    clean_hub_credit = [i for i in hub_credit if i[0].isalpha()]
    clean_info = clean_info[:-1] + [clean_hub_credit]
    return f'{clean_info}'


@app.route('/filter', methods=['GET'])
def filter():
    con = sqlite3.connect('BUClass_API/class_storage.db')
    cur = con.cursor()
    info = ''

    req = request.args.get('prereq')
    if req:
        info = cur.execute(f'SELECT Name \
                            FROM ClassData \
                            WHERE Prereq like "%{req}%"')

    if info:
        return f'{[i[0] for i in info.fetchall()]}'
    else:
        return 'No results found.'


if __name__ == '__main__':
    # Local testing
    app.run(host='127.0.0.1', port=8080, debug=True)
