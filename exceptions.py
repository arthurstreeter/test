class EventOutOfBoundsError(Exception):
    """event end occurs past MAX_AXIS_SIZE"""

    pass


class InvalidEventsError(Exception):
    """if events are not passed in as a list to create Axis class"""

    pass


class InvalidAxesError(Exception):
    """if axes are not passed in as a dict to create Report class"""

    pass
