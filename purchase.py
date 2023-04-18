from flask import Flask, render_template, request, redirect
import json
import pandas as pd

app = Flask(__name__)

import pandas as pd

@app.route('/book/<flight_number>', methods=['GET', 'POST'])
def book(flight_number):
    flight_data = pd.read_excel('flight_data.xlsx')

    flight = flight_data[flight_data['flight_number'] == flight_number]

    if request.method == 'POST':
        return redirect('/confirmation')

    return render_template('book.html', flight=flight)


@app.route('/flights', methods=['POST'])
def flights():
    with open('flight_data.json') as f:
        flight_data = json.load(f)

    origin = request.form['origin']
    destination = request.form['destination']
    departure_date = request.form['departure_date']

    filtered_data = [flight for flight in flight_data if flight['origin'] == origin and flight['destination'] == destination and flight['departure_date'] == departure_date]

    return render_template('flights.html', flights=filtered_data)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
