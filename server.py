from flask import Flask, render_template
from opentok import OpenTok

app = Flask(__name__)

API_KEY = ""
SECRET = ""

opentok = OpenTok(API_KEY, SECRET)

ROOMS = {}

@app.route('/<room>')
def room(room):
    if room in ROOMS:
        session_id = ROOMS[room]
    else:
        session_id = opentok.create_session().session_id
        ROOMS[room] = session_id

    print session_id
    token = opentok.generate_token(session_id)
    return render_template('room.html',
                           api_key=API_KEY, session_id=session_id, token=token)

if __name__ == '__main__':
    app.run()
