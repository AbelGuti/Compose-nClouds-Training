from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'database',
    'user': 'root',
    'password': 'cases123',
    'database': 'case_studies',
}

# Route to display data from the database
@app.route('/')
def show_data():
    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)

        # Create a cursor to execute SQL queries
        cursor = connection.cursor(dictionary=True)

        # Execute a query to fetch data (assuming a table named 'example')
        cursor.execute("SELECT * FROM case_studies")

        # Get all the results
        results = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Render an HTML template with the obtained data
        return render_template('show_data.html', results=results)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
