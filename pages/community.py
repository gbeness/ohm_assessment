from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User

import mysql.connector
'''
Potential implentation to create table object and pass it as
argument to render_template(). This approach will require
editing of requirements.txt to include Flask-Table = 0.2.9.
Documentation can be found:
https://flask-table.readthedocs.io/en/stable/

from flask_table import Table, Col

class UserTable(Table):
    name = Col('Name')
    tier = Col('Tier')
    points = Col('Points')
    phone_numbers = Col('Phone Number(s)')

class Row(object):
    def __init__(self, name, tier, points, phone_numbers):
        self.name = name
        self.tier = tier
        self.points = points
        self.phone_numbers = phone_numbers
'''

@app.route('/community', methods=['GET'])
def community():

    login_user(User.query.get(1))
    table_body = []
    try:
        db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="reallyStrongPassword",
                    database="ohm_assessment"
        )

        cursor = db.cursor()
        cursor.execute('''SELECT display_name, tier, point_balance, attribute
                          FROM ohm_assessment.user
                          LEFT JOIN (
                                      SELECT user_id, GROUP_CONCAT(attribute SEPARATOR ' ') AS attribute
                                      FROM ohm_assessment.rel_user_multi
                                      WHERE rel_lookup='Phone'
                                      GROUP BY user_id
                                    ) AS temp
                          ON user.user_id=temp.user_id
                          ORDER BY signup_date DESC;
                          ''')


        row = cursor.fetchone()
        num_users_to_display = 5
        for i in range(num_users_to_display):
            if row is None:
                break
            else:
                (name, tier, points, phone) = row
                table_body.append([name, tier, points, phone.split(' ') if phone != None else['']])
            row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        db.close()

    return render_template("community.html", table=table_body)

