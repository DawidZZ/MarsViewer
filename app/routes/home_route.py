from app import app

@app.route('/')
def home():
    return "<h1> Hello poor student! </h1>"