from flask import Flask, request, redirect, render_template, Response, flash
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime

app = Flask(__name__)
app.secret_key = "c678sss"

status_record = {}

@app.route("/sms", methods=['GET', 'POST'])
def reply_to_incoming_text():

    resp = MessagingResponse()

    resp.message("Hello! Is it me you're looking for?")
    
    return str(resp)

@app.route("/status", methods=['GET','POST'])
def respond():
    del_status=request.values.get('MessageStatus')
    print(del_status)
    sms_id=request.values.get('SmsSid')
    print(sms_id)
    t = datetime.now()
    timestamp = t.strftime("%Y%m%d %H:%M:%S")
    print(timestamp)
    status_record[del_status] = timestamp
    print(status_record)

    
    if request.method == "POST:":
        return Response(status=200)    

    return render_template('index.html', sms_id=sms_id, status_record=status_record)


if __name__ == "__main__":
    app.run(debug=True)