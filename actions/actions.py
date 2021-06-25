# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import requests
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import requests

        response = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        state = None
        for e in entities:
            if e['entity'] == 'state':
                state = e['value']
                break

        for data in response['statewise']:
            if data['state'] == state.title():
                print(data)


        message = "Active case are {}".data['active']
        print(message)
        dispatcher.utter_message(text="Hello Wun actionorld!  {}".format(state))

        return []
