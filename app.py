import os
import psycopg2

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route('/', methods=('GET', 'POST'))
def index():
    # Connect to database
    conn = psycopg2.connect(host='db', database=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'])
    cur = conn.cursor()

    # Get number of all GET requests
    sql_success_counts = """SELECT source, COUNT(*) FROM weblogs WHERE status LIKE \'2__\' GROUP BY source;"""
    cur.execute(sql_success_counts)
    success_counts = dict(cur.fetchall())

    sql_total_counts = """SELECT source, COUNT(*) FROM weblogs GROUP BY source"""
    cur.execute(sql_total_counts)
    total_counts = dict(cur.fetchall())

    sources = {'remote', 'local'}
    rates = {source: success_counts[source] / total_counts[source] if source in total_counts else 'No entries yet!' for source in sources}

    return render_template('index.html', local_rate=rates['local'], remote_rate=rates['remote'])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
