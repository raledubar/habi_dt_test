from flask import Flask, request, jsonify, make_response
import pymysql
import json


app = Flask(__name__)


def get_connection():
    return pymysql.connect(
        host='3.130.126.210',
        port=3309,
        user='pruebas',
        password='VGbt3Day5R',
        database='habi_db',
    )


@app.route('/inmuebles', methods=['GET'])
def get_inmuebles():
    connection = get_connection()
    with connection.cursor() as cursor:
        read = cursor.execute("SELECT * FROM habi_db.status_history")
        if read:
            print("read in terminal")
            print(read)
            return f"I have read the table"
        return f"I CAN NOT READ THE TABLE"


if __name__ == '__main__':
    app.run(debug=True)
