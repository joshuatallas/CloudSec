
from flask import Flask, request, jsonify
import psycopg
import json

app = Flask(__name__)

conn = psycopg.connect("dbname='postgres' user='postgres' password='password' host='localhost' port='5433'")
cur = conn.cursor()


#cur.execute("CREATE TYPE decision_enum as ENUM ('allow', 'deny');")

@app.route('/policies', methods=['POST'])
def insert_policy():
    
    data = request.get_json()

    policy_name = data.get('policy_name')
    tenant = data.get('tenant')
    subject = data.get('subject')
    policy_description = data.get('policy_description')
    action = data.get('action')
    created_by = data.get('created_by')
    policy_type = data.get('policy_type')
    policy_schema = data.get('policy_schema')
    resource = json.dumps(data.get('resource', {}))
    decision = data.get('decision')
    created = data.get('created')
    last_updated = data.get('last_updated')
    owner = data.get('owner')
    project = data.get('project')
    
    cur.execute("""
        INSERT INTO policies (
            policy_name,
            tenant,
            subject,
            policy_description,
            action,
            created_by,
            policy_type,
            policy_schema,
            resource,
            decision,
            owner,
            project
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        ) RETURNING *;
    """, (
        policy_name,
        tenant,
        subject,
        policy_description,
        action,
        created_by,
        policy_type,
        policy_schema,
        resource,
        decision,
        owner,
        project
        created_by,
        policy_type,   
        ))

    conn.commit()
    return jsonify({"message": "Policy created successfully"
        
        })
        

@app.route('/policies/search', methods=['GET'])
def search_policies():

    conn = psycopg.connect("dbname='postgres' user='postgres' password='password' host='localhost' port='5433'")
    cur

    fields = "policy_name,policy_id,decision,tenant,uuid"
    policy_columns = fields.split(',')

    policy_id = request.args.get('policy_id')
    decision = request.args.get('decision')
    tenant = request.args.get('tenant')
    uuid = request.args.get('uuid')
    policy_name = request.args.get('policy_name')
    #project = request.args.get('project')
    #owner = request.args.get('owner')
    #policy_description = request.args.get('policy_description')
    #created = request.args.get('created')

    query = f"SELECT {fields} FROM policies WHERE 1=1"
    params = []

    if policy_id:
        query += " AND policy_id = %s"
        params.append(policy_id)
    if decision:
        query += " AND decision = %s"
        params.append(decision)
    if tenant:
        query += " AND tenant = %s"
        params.append(tenant)
    if uuid:
        query += " AND uuid = %s"
    if policy_name:
        query += " AND policy_name = %s"
        params.append(policy_name)
   # if project:
   #     query += " AND project = %s"
   #     params.append(project)
   # if owner:
   #     query += " AND owner = %s"
   #     params.append(owner)
   # if policy_description:
   #     query += " AND policy_description = %s"
   #     params.append(policy_description)
   # if created:
   #     query += " AND created = %s"
   #     params.append(created)


    cur.execute(query, params)
    policies = cur.fetchall() 

    result = []
    for policy in policies:
        policy_dict = dict(zip(policy_columns, policy))
        result.append(policy_dict)
   
    return jsonify({'policies': result})




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

"""@app.route('/policies/owner/<owner>', methods=['GET'])
def get_policies_owner(owner):

    conn = psycopg.connect("dbname='postgres' user='postgres' password='password' host='localhost' port='5433'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM policies WHERE owner = %s;", (owner,))
    policies = cur.fetchall() 
    return str(policies)"""





if __name__ == '__main__':
    app.run(debug=True, port=5001)



