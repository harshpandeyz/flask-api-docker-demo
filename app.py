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
# change 16606
# change 16259
# change 5095
# change 4965
# change 3916
# change 26809
# change 14230
# change 283
# change 14953
# change 20950
# change 15509
# change 11372
# change 20194
# change 21217
# change 5534
# change 18970
# change 20902
# change 10283
# change 2556
# change 16446
# change 22063
# change 1817
# change 32678
# change 8463
# change 1111
# change 30465
# change 3001
# change 6210
# change 3788
# change 1166
# change 24228
# change 15773
# change 16347
# change 6880
# change 754
# change 29369
# change 12176
# change 28508
# change 13418
# change 14286
# change 12908
# change 5242
# change 8472
# change 4949
# change 26496
# change 1349
# change 19869
# change 1434
# change 21533
# change 20959
# change 5193
# change 29357
# change 17167
# change 16397
# change 12313
# change 12988
# change 31424
# change 32636
# change 18980
# change 24665
# change 18788
# change 16059
# change 31645
# change 23265
# change 17907
# change 1414
# change 5658
# change 176
# change 878
# change 8574
