from main import app

@app.route('/')
def index():
    return "Hooray"

@app.route('/fish/<id>')
def get_fish(id):
    print(id)
    return "my fish is gorgeous"

@app.route('/fish', method = ['GET'])
def get_all_fishes():
    return "all fish"

@app.route('/fish', method=['POST'])
def create_fish():
    print('fish created!')