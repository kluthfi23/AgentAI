class Action:

    def __init__(self, action, data=None):

        self.action = action
        self.data = data or {}


    def to_dict(self):

        return {
            "action": self.action,
            "data": self.data
        }