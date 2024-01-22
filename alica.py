from flask import Flask, request
import logging
import json

app = Flask('app')

@app.route('/')
def hello_world():
  logging.info(request.json)

  response = {
      "version": request.json["version"],
      "session": request.json["session"],
      "response": {
          "end_session": False
      }
  }

  req = request.json
  if req["session"]["new"]:
      response["response"]["text"] = "Привет! Как твои дела? Как отметил новый год?"
  else:
      if req["request"]["original_utterance"].lower() in ["хорошо", "отлично"]:
          response["response"]["text"] = "Супер! Я за вас рада!"
      elif req["request"]["original_utterance"].lower() in ["плохо", "скучно"]:
          response["response"]["text"] = "Это печально... нужно было позвать меня!"

  return json.dumps(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

