
import psycopg2
import json 


db_name = 'properties'
db_user = 'postgres'
db_pass = 'postgres'
db_host = 'postgres'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)


if __name__ == "__main__":
    conn = psycopg2.connect(db_string)
    cur = conn.cursor()
    
    with open('props.json') as f:
        data = json.loads(f.read())
    
    # print(data)
    for d in data:
        cur.execute(f"INSERT INTO props (prop_name, img_src) VALUES ('{d['name']}', '{d['img_src']}');")
        

    conn.commit()
    conn.close()
    