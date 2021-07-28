from flask import Flask, Blueprint, request



app = Flask(__name__)
app_bp = Blueprint('app_bp', __name__)


@app_bp.route('/test', methods=['GET'])
def test_api():
    return {'id': 123}

@app_bp.route('/home', methods=['GET'])
def home():
    data = request.args.to_dict()
    return {'id': int(data['id'])}


app.register_blueprint(app_bp)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

# def create_app():
#     return app
