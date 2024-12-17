from flask import Flask, request, jsonify, send_file
from database import Database
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
db = Database("users")


@app.route(rule="/get-user-data", methods=["POST"])
def handle_request():
    data = request.get_json()
    uid = data["uid"]
    print(uid)
    response = db.get_user(uid)
    if response["exists"]:
        db.mark_user_as_arrived(uid)

    print(response)
    return jsonify(response)


@app.route('/get-image', methods=['POST'])
def fetch_image():
    data = request.get_json()
    imagePath = data["image_link"]
    print("image fetched")
    return send_file('$HOME/Students/'+ imagePath, mimetype='image/jpeg')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=2399, ssl_context=("localhost.pem", "localhost-key.pem"))

