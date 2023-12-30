from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Replace with the actual direct radio stream URLs
    radio_stations = {
        'Glz Redio': 'http://glzwizzlv.bynetcdn.com/glglz_mp3',  # GLZ Radio
        'Galei Zahal Redio': 'http://glzwizzlv.bynetcdn.com/glz_mp3'  # Galei Israel
    }
    return render_template('index.html', radio_stations=radio_stations)

if __name__ == '__main__':
    app.run(port=30924, debug=True)
