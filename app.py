from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from Python Flask App")

@app.route("/api/hello")
def hello():
    return jsonify(status="success", message="As per your application")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)# change 17049
# change 5645
# change 15338
# change 16197
# change 12590
# change 27635
# change 10264
# change 19847
# change 1913
# change 3422
# change 3011
# change 12149
# change 6836
# change 5079
# change 11442
# change 19376
# change 13817
# change 13489
# change 31764
# change 26548
# change 14666
# change 8559
# change 17222
