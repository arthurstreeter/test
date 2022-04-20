
class Event:
    def __init__(self, start: int, duration: int):
        """instantiate Event class

        Args:
            start: shall be an integer >= 0, else throw a ValueError exception
            duration: shall be an integer > 0, else throw a ValueError exception

        Raises:
            ValueError: if start/duration specifications are not met
        """
        # TODO: implement this
        pass

    def __lt__(self, obj) -> bool:
        """is self's start before obj's start?

        Args:
            obj: Event instance to compare against

        Returns:
            whether self occurs before obj
        """
        return self.start < obj.start

    def __eq__(self, obj) -> bool:
        """is self's start and duration equal to obj's start and duration?

        Args:
            obj: Event instance to compare against

        Returns:
            whether self is the same start/duration as obj
        """
        return self.start == obj.start and self.duration == obj.duration

    def __repr__(self) -> str:
        return f"<Event start={self.start}, duration={self.duration}>"
