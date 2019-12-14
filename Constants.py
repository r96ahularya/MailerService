SENDER = "your email"     # me == my email address
PASSWORD = "your password"
RECEIVER = "receiver 1"     # you == recipient's email address
RECEIVER_LIST = ["receiver 1", "receiver 2"]

PROTOCOL = "smtp.gmail.com"
PORT = 587

SUBJECT = "Offers for YOU!!"

SAMPLE_PAYLOAD = {
    "receiver 1" : {
        "FIRST_NAME" : "Bob",
        "LAST_NAME" : "Sharma"
    },
    "receiver 2" : {
        "FIRST_NAME" : "Builder",
        "LAST_NAME" : "Jain"
    }
}

SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>Hello {FIRST_NAME} {LAST_NAME}</p>
<p>Thank you Mr./Ms. {LAST_NAME}</p>

</body>
</html>"""
