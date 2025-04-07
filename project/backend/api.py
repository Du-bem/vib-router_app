from fastapi import FastAPI
import psycopg2
from fastapi import Query

connection = psycopg2.connect(
    dbname="mydb",
    user="user",
    password="password",
    host="127.0.0.1",
    port="5432"
)

app = FastAPI()


@app.get("/get-user")
async def get_user_by_email(email: str = Query(..., description="The email of the user to retrieve")):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            if user:
                return {
                    "id": user[0],
                    "name": user[1],
                    "email": user[2],
                    "password_hash": user[3]
                }
            else:
                return {"error": "User not found"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/login")
async def login(email: str, password: str):
    try:
        res = get_user_by_email(email)
        return res
    except Exception as e:
        return {"error": str(e)}

