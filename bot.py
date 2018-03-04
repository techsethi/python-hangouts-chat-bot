#!/usr/bin/env python3
"""Example bot that returns a synchronous response."""

from flask import Flask, request, json
import pprint

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bot would respond to post requests!"

@app.route('/', methods=['POST'])
def on_event():
  """Handles an event from Hangouts Chat."""
  event = request.get_json()
  # pp = pprint.PrettyPrinter(depth=6)
  # pp.pprint(event)
  if event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'ROOM':
    text = 'Thanks for adding me to "%s"!' % event['space']['displayName']
  elif event['type'] == 'MESSAGE':
    text = 'Hello %s, How are you. You said: `%s`' % (event['message']['sender']['displayName'].split(" ")[0],event['message']['text'])
  else:
    return
  return json.jsonify({'text': text})

if __name__ == '__main__':
  app.run(debug=True)
