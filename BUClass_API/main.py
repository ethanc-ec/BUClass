"""Main file for the BUClass_API."""

from pathlib import Path

from flask import Flask, request
from google.cloud import bigquery

app = Flask(__name__)
parent_dir = Path(__file__).parent
project = ''
table = ''
client = bigquery.Client(project=project)


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

    QUERY = (
        "select *"
        f"from `{table}`"
        f"where course = '{req}'")

    query_job = client.query(QUERY)
    rows = query_job.result()

    return [list(row) for row in rows]


@app.route('/find', methods=['GET'])
def find():
    """Filter classes by prereq, coreq, credit, and hub credits."""

    query = [
        'prereq',
        'coreq',
        'credit',
        'hub_credit'
    ]

    base, count = f'SELECT course FROM `{table}` WHERE', 0

    for section in query:
        req = request.args.get(section)

        if req and count > 0:
            base += ' AND'
        count += 1

        if req and section in ['prereq', 'coreq']:
            input = req.replace(' ', '')
            
            if len(input) == 5:
                input = f'{input[0:2]} {input[2:]}'
            elif len(input) == 8:
                input = f'{input[0:3]} {input[3:5]} {input[5:]}'
            
            base += (f" CONTAINS_SUBSTR({section}, '{input}')")

        elif req and section == 'credit':
            base += (f' {section} = "{req}"')

        elif req and section == 'hub_credit':
            base += (f" CONTAINS_SUBSTR({section}, '{req}')")

    query_job = client.query(base)

    rows = [list(row) for row in query_job.result()]

    if len(rows) != 0:
        return rows

    return 'No classes found.'


if __name__ == '__main__':
    # Local testing
    app.run(host='127.0.0.1', port=8080, debug=True)
