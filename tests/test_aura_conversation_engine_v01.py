from core.conversation.aura_conversation_engine_v01 import (

    AURAConversationEngine

)

def test_conversation_engine():

    engine = AURAConversationEngine()

    conversation = engine.start_conversation(

        "Test User"

    )

    result = engine.process_message(

        conversation["id"],

        "Help me plan my week"

    )

    print("AURA Conversation Engine Test")

    print("-----------------------------")

    print(result)

if __name__ == "__main__":

    test_conversation_engine()