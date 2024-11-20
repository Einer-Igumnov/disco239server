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
    return send_file('images/' + imagePath, mimetype='image/jpeg')


@app.route('/renew-users', methods=['POST'])
def renew_users():
    db.mark_all_users_as_not_arrived()


if __name__ == "__main__":
    db.mark_all_users_as_not_arrived()
    app.run(host="192.168.0.110", debug=True, port=2399, ssl_context=("localhost.pem", "localhost-key.pem"))

