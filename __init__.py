from mycroft import MycroftSkill, intent_file_handler


class ChatgptBridge(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bridge.chatgpt.intent')
    def handle_bridge_chatgpt(self, message):
        self.speak_dialog('bridge.chatgpt')


def create_skill():
    return ChatgptBridge()

