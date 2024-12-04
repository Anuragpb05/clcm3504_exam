from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Database connection details
DB_HOST = "your-rds-endpoint"
DB_USER = "your-username"
DB_PASSWORD = "your-password"
DB_NAME = "your-database-name"

@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Extract form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    try:
        # Connect to RDS
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()

        # Insert data into the database
        query = "INSERT INTO submissions (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, message))
        connection.commit()

        return jsonify({"status": "success", "message": "Form data stored successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)



