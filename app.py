from flask import Flask

app = Flask('webapp')

@app.route('/')
def home():
    return "My Project"

if __name__ == '__main__':
    app.run(debug=True)