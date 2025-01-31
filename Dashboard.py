from flask import Flask, render_template

app = Flask(__name__)

# Route for the main dashboard page
@app.route('/')
def dashboard():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
