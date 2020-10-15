from flask import Flask, jsonify, request
from flask_cors import CORS
from crontab import CronTab
from datetime import datetime

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

CORS(app, resources={r'/*': {'origins': '*'}})

cron = CronTab(user='pi')

def pull_jobs():
    tweets = []

    for job in cron:

        if ('tweeter.py' not in str(job)):
            continue

        tokens = str(job).split(' ')

        hour = tokens[1]
        minute = tokens[2]

        d = ''
        if (minute == '*'):
            d = datetime.strptime(hour, "%H")
        else:
            d = datetime.strptime(hour + ":" + minute, "%H:%M")

        tweet = tokens[7:]
        hashtag = tweet[len(tweet) - 1].replace('"', '')

        tweets.append({'tweet' : hashtag, 'time' : d.strftime("%-I:%M %p")})

    return jsonify(tweets)

@app.route('/today')
def get_today():
    return pull_jobs()

@app.route('/delete/<hashtag>')
def delete(hashtag):
    for job in cron:
        if (hashtag in str(job)):
            cron.remove(job)
    return pull_jobs()

if __name__ == '__main__':
    app.run(host='192.168.0.22')
