from collections import defaultdict

class EventBus:

    """

    Central communication system for AURA.

    """

    def __init__(self):

        self.listeners = defaultdict(list)

    def subscribe(self, event_type, callback):

        self.listeners[event_type].append(callback)

    def publish(self, event):

        handlers = self.listeners.get(

            event.event_type,

            []

        )

        for handler in handlers:

            handler(event)