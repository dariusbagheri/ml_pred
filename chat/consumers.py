import json

import requests
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to ChatGPT API
        response = self.send_to_chatgpt(message)

        # Extract the response message from the API response
        response_message = response["message"]

        # Send the response back to the WebSocket client
        self.send(text_data=json.dumps({"message": response_message}))

    def send_to_chatgpt(self, message):
        # Make a POST request to the ChatGPT API
        api_url = "YOUR_CHATGPT_API_URL"
        headers = {"Content-Type": "application/json"}
        data = json.dumps({"message": message})
        response = requests.post(api_url, headers=headers, data=data)

        # Parse the JSON response
        response_json = response.json()

        return response_json
