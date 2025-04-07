import psycopg2

connection = psycopg2.connect(
    dbname="mydb",
    user="user",
    password="password",
    host="172.19.0.2",
    port="5432"
)


print(connection)

def get_user(username):
    
