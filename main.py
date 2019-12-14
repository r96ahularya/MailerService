from SendMail import *
from flask import *
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/check', methods=['GET'])
def check():
    return "<h1>OK</h1>"

@app.route('/sendmail', methods=['POST'])
def mailer():
    sendEmail()
    return jsonify(status = 200, isMailSent = True)

app.run(host='0.0.0.0', port = 8000)
