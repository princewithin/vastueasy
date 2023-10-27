from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder= 'static')

@app.route('/')
def first_page():
    return render_template('index.html')
@app.route('/vastu_shastri')
def bio_page():
    return render_template('vastu_shastri.html')

if __name__ == '__main__':
    app.run(debug=True)