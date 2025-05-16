from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('ab.html')

@app.route('/submit', methods=['POST'])
def submit():
    height =float(request.form['height'])
    weight = float(request.form['weight'])
    BMI = weight / (height *height)
    return f"Your BMI is {BMI}"

    
if __name__ == '__main__':
    app.run(debug=True)