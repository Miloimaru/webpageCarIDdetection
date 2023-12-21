from flask import Flask, render_template, Response, jsonify, request, session, send_file
import cv2
from YoLo.YoLo2 import video_detection
from PIL import Image
import io
import sqlite3
import base64

app = Flask(__name__)

app.config['SECRET_KEY'] = 'muhammadmoin'
app.config['UPLOAD_FOLDER'] = 'static/files'

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/show_data', methods=['POST'])
def show_data():
    selected_day = request.form['day']
    selected_month = request.form['month']
    selected_year = request.form['year']

    selected_date = f"{selected_year}-{selected_month.zfill(2)}-{selected_day.zfill(2)}"

    # Fetch data from SQLite
    conn = sqlite3.connect('../pythonProject1/SQLite/Data_test1.db')
    try:
        cursor = conn.cursor()

        query = f"SELECT Date,image,car_ID FROM medal WHERE Date = ? ORDER BY ID"
        cursor.execute(query, (selected_date,))
        data = cursor.fetchall()

        conn.close()

        decoded_data = []
        for row in data:
            # Convert blob data (image) to base64 for HTML display
            date = row[0]
            picture = base64.b64encode(row[1]).decode('utf-8') if row[1] else None
            car_id = row[2]
            decoded_data.append((date, picture, car_id))

        return render_template('Show_data.html', data=decoded_data)
    except sqlite3.Error as error:
        print("Error: ", error)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    app.run(debug=True)
