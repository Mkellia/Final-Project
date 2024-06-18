import os
from flask import Flask
from waste_manage.routes import bp

app = Flask(__name__)

# Configuration and other setup if needed

# Register the blueprint with the app
app.register_blueprint(bp)

@app.route('/')
def index():
    return 'Welcome to Our Waste Management Platform'

if __name__ == '__main__':
    app.run(debug=True)
