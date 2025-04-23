from flask import Flask, render_template

app = Flask(__name__)

# 首页
@app.route('/')
def home():
    return render_template('home_test.html')

# ISO 页面
@app.route('/iso')
def iso_page():
    return render_template('iso.html')

# Shutter Speed 页面
@app.route('/ss')
def shutter_speed_page():
    return render_template('ss.html')

# Aperture 页面
@app.route('/aperture')
def aperture_page():
    return render_template('aperture.html')

# Simulator 页面
@app.route('/simulator')
def simulator_page():
    return render_template('simulator.html')

# Quiz 页面
@app.route('/quiz')
def quiz_page():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)
