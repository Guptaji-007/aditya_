from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

@app.route('/')
def get_data():
    try:
        # Establish MySQL connection
        timeout = 10
        connection = pymysql.connect(
            charset="utf8mb4",
            connect_timeout=timeout,
            cursorclass=pymysql.cursors.DictCursor,
            db="WEBSITE",
            host="mysql-14da71f7-devmittal9705-d8fc.d.aivencloud.com",
            password="AVNS_M8EGsbDUEeMajooE7YC",
            read_timeout=timeout,
            port=22874,
            user="avnadmin",
            write_timeout=timeout,
        )

        cur = connection.cursor()
        cur.execute("SELECT * FROM Aditya;")
        data = cur.fetchall()
        connection.close()

        return jsonify(data)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)