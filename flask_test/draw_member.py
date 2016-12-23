import csv
import sqlite3
import random
from flask import Flask, g ,render_template, request

app = Flask(__name__)
SQLITE_DB_PATH = 'members.db'
SQLITE_DB_SCHEMA = 'create_db.sql'
MEMBER_CSV_PATH = 'members.csv'


def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(SQLITE_DB_PATH)
		db.execute("PRAGMA foreign_keys = ON")
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/draw', methods=['POST'])
def draw():
	db = get_db()

	group_name = request.form.get('group_name', 'ALL')
	valid_members_sql = 'select id from members'
	if group_name == 'ALL':
		cursor = db.execute(valid_members_sql)
	else:
		valid_members_sql += ' where group_name = ?'
		cursor = db.execute(valid_members_sql,(group_name,))
	valid_member_ids = [
		row[0] for row in cursor
	]

	if not valid_member_ids:
		err_msg = "<p>No members in group '%s' </p>" % group_name
		return err_msg,404

	lucky_member_id = random.choice(valid_member_ids)

	member_name, member_group_name = db.execute(
		'select name, group_name from members where id =?',
		(lucky_member_id,)
		).fetchone()


	return render_template(
		'draw.html',
		name=member_name,
		group=member_group_name,
	)


	@app.route('/history')
	def history():
	    db = get_db()
	    recent_histories = db.execute(
	        'SELECT m.name, m.group_name, d.time '
	        'FROM draw_histories AS d, members as m '
	        'WHERE m.id == d.memberid '
	        'ORDER BY d.time DESC '
	        'LIMIT 10'
	    ).fetchall()
	    return render_template(
	        'history.html',
	        recent_histories=recent_histories
	    )	

if __name__ == '__main__':
	app.run(debug=True)


