
class Timeline:
    size = 20  # total size of the timeline, events may not end at or beyond this point

    def __init__(self, events: list):
        """list of events to set as self.events

        Args:
            events: list of Event instances

        Raises:
            exceptions.InvalidEventsError: if `events` is not a list or events overlap
            exceptions.EventOutOfBoundsError: if an event ends beyond Timeline.size
        """
        # TODO: implement

    def check_out_of_bounds(self, events: list):
        """check all events in list for whether they go beyond Timeline.size

        Args:
            events: list of Events to evaluate

        Raises:
            EventOutOfBoundsError: if event is OOB
        """
        # TODO: implement

    def check_overlapping(self, events: list):
        """raise exception if any events are overlapping

        Args:
            events: list of Events to evaluate

        Raises:
            exceptions.InvalidEventsError: if events are overlapping
        """
        # TODO: implement

    def get_duration_stats(self) -> dict:
        """calculate the minimum and maximum event durations as well as the percentage
        of the timeline that events are scored

        Returns:
            dict containing duration stats in the form:
                {
                    "min": <int>,
                    "max": <int>,
                    "percent": <float between 0 and 100>
                }
        """
        # TODO: implement

    def __repr__(self) -> str:
        return f"<Timeline events={self.events}>"


if __name__ == "__main__":
    from event import Event
    
    # example usage
    timeline = Timeline(
        events=[
            Event(start=0, duration=1),
            Event(start=4, duration=4),
        ]
    )
    print(timeline)
    duration_stats = timeline.get_duration_stats()
    print(duration_stats)
    
    breakpoint()