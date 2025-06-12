from flask import Flask, request
import psycopg
import json

app = Flask(__name__)


#cur.execute("CREATE TYPE decision_enum as ENUM ('allow', 'deny');")

@app.route('/policies', methods=['POST'])
def insert_policy():

    conn = psycopg.connect("dbname='postgres' user='postgres' password='password' host='localhost' port='5433'")
    cur = conn.cursor()
    
    data = request.get_json()

    json_data = json.dumps(data['resource'])


    cur.execute("""INSERT INTO policies(policy_name, tenant, subject, policy_description, action, created_by, policy_type, policy_schema, uuid, resource, decision)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (data['policy_name'], data['tenant'], data['subject'], data['policy_description'], data['action'], data['created_by'], data['policy_type'], data['policy_schema'], data['uuid'], json_data, data['decision'], data['owner'], data['project']))

    conn.commit()
    return "Policy created successfully!"


@app.route('/policies/<policy_id>', methods=['DELETE'])
def delete_policy(policy_id):

    conn = psycopg.connect("dbname='postgres' user='postgres' password='password' host='localhost' port='5433'")
    cur = conn.cursor()


    cur.execute("DELETE FROM policies WHERE policy_id = %s", (policy_id,))
    conn.commit()
    return "Policy deleted"

@app.route('/policies/<int:policy_id>', methods=['GET'])
def get_policy(policy_id):

    conn = psycopg.connect("dbname='postgres' user='postgres' password='password' host='localhost' port='5433'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM policies WHERE policy_id = %s", (policy_id,))
    conn.commit()
    policies = cur.fetchone()
    return str(policy)

@app.route('/policies/owner/<owner>', methods=['GET'])
def get_policies_owner(owner):

    conn = psycopg.connect("dbname='postgres' user='postgres' password='password' host='localhost' port='5433'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM policies WHERE owner = %s;", (owner,))
    policies = cur.fetchall() 
    return str(policies)





if __name__ == '__main__':
    app.run(debug=True, port=5001)



#python text to insert data
#insert_policy(policy_name='File-Restriction', tenant='TACC', subject='developer007', policy_description='Restricts developer access to Files', action='database connection', created_by='Hank Hill',policy_type='Network', policy_schema='version 3', uuid='j478y4h007', resource={'network': 'File-db', 'Files': 'database-2'}, decision='allow', owner='JTallas', project='Test Policy Project')


#cur.execute("""CREATE TABLE policies(policy_id SERIAL PRIMARY KEY, policy_name VARCHAR(100) NOT NULL, tenant VARCHAR(100)NOT NULL, subject VARCHAR(100) NOT NULL, policy_description VARCHAR(2048), action VARCHAR(50), created_by VARCHAR(100) NOT NULL, policy_type VARCHAR(50) NOT NULL, policy_schema VARCHAR(100) NOT NULL, uuid VARCHAR(64) NOT NULL, resource JSON, decision decision_enum NOT NULL, created timestamp without time zone NOT NULL DEFAULT(now() at time zone 'utc'), last_updated timestamp without time zone NOT NULL DEFAULT(now() at time zone 'utc'));""")












#def view_all_policies():
#    cur.execute("SELECT * FROM policies;")
#    policies = cur.fetchall()
#    for policy in policies:
#        print(policy)

#def add_new_column(column_name, column_type): 
#    cur.execute(f"ALTER TABLE policies ADD COLUMN {column_name} {column_type};")

#def delete_column(column_name):
#    cur.execute(f"ALTER TABLE policies DROP COLUMN {column_name};")






