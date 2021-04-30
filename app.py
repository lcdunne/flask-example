from flask import Flask, request
from flask_mail import Mail, Message
from threading import Thread


app = Flask(__name__)
app.config.from_object('config.BaseConfig')
mail = Mail(app)


@app.route('/')
def index():
    return "Index page"


def _send_email(app, to, message):
    with app.app_context():
        msg = Message(message, recipients=[to])
        try:
            mail.send(msg)
            status = True
        except Exception as e:
            print(e)
            status = False
        return status


@app.route('/send')
def send_email():
    to = request.args.get('email')
    print("\nAttempting to send to: ", to)
    Thread(target=_send_email, args=(app, to, "Hello")).start()
    # email_status = _send_email(to=to, message="Hello")
    # if email_status:
    #     return "Email sent"
    # else:
    #     return "Email failed"
    return "Ok."

# # This route is an example from https://sendgrid.com/blog/sending-emails-from-python-flask-applications-with-twilio-sendgrid/
# @app.route('/send', methods=['GET', 'POST'])
# def send_message():
#     if request.method == 'POST':
#         recipient = request.form['recipient']
#         print(recipient)
#         msg = Message('Twilio SendGrid Test Email', recipients=[recipient])
#         msg.body = ('Congratulations! You have sent a test email with '
#                     'Twilio SendGrid!')
#         msg.html = ('<h1>Twilio SendGrid Test Email</h1>'
#                     '<p>Congratulations! You have sent a test email with '
#                     '<b>Twilio SendGrid</b>!</p>')
#         mail.send(msg)
#         # flash(f'A test message was sent to {recipient}.')
#     return "Email page"


if __name__ == '__main__':
    app.run(debug=True)
