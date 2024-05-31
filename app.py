from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Replace with the actual direct radio stream URLs
    radio_stations = {
        'Glz Radio': 'http://glzwizzlv.bynetcdn.com/glglz_mp3',  # GLZ Radio
        'Galei Zahal Radio': 'http://glzwizzlv.bynetcdn.com/glz_mp3'  # Galei Zahal Radio
    }
    return render_template('index.html', radio_stations=radio_stations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30924, debug=True)
