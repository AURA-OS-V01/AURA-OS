from agents.communication.message_bus import MessageBus

def test_message_bus():

    bus = MessageBus()

    message = bus.send(

        "Security Agent",

        "Owner Agent",

        "Detected possible vulnerability"

    )

    print("Message Bus Test")

    print("----------------")

    print(message)

if __name__ == "__main__":

    test_message_bus()