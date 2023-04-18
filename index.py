from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/book/<flight_number>', methods=['GET', 'POST'])
def book(flight_number):
    with open('flight_data.json') as f:
        flight_data = json.load(f)

    flight = next((flight for flight in flight_data if flight['flight_number'] == flight_number), None)

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

if __name__ == '__main__':
    app.run(debug=True)
