from flask import Flask, request, render_template, abort,jsonify
# from flask_ngrok import run_with_ngrok
# from flask_cors import CORSi
from Databse import user_insert

app = Flask(__name__)
# run_with_ngrok(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST','get'])
def webhook():
    data = request.get_json();
    print(data)
    print("webhook")

    da=user_insert(data)
    # print(da)
    return jsonify({
        "fulfillmentText":da,
        "source":"webhookdata"
    })

    # return data

# @app.route('/')
# def testbot():
#
#     return 'Hello, World!'

if __name__ == "__main__":
    app.run()
# <<<<<<< HEAD

# if __name__ == "__main__":
#     app.run(debug=True,host="0.0.0.0", port=80)
# =======
# >>>>>>> parent of d7f71b0 (update)
