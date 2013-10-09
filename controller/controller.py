class Controller:
    """
    base class for all parts of controller
    """

    def __init__(self, model):
        """
        :param model: object to be displayed by this particular controller
        """
        self.model = model
        pass

    def display(self):
        """
        present element on the screen
        """
        #to be implemented by inheriting views
        pass