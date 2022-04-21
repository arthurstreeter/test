from operator import index
import exceptions

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

        if not isinstance(events, list):
            raise exceptions.InvalidEventsError()

        self.check_out_of_bounds(events)
        self.check_overlapping(events)

        self.events = events


    def check_out_of_bounds(self, events: list):
        """check all events in list for whether they go beyond Timeline.size

        Args:
            events: list of Events to evaluate

        Raises:
            EventOutOfBoundsError: if event is OOB
        """
        # TODO: implement
        for event in events:
            end_time = event.start + event.duration
            if end_time > Timeline.size:
                raise exceptions.EventOutOfBoundsError()


    def check_overlapping(self, events: list):
        """raise exception if any events are overlapping

        Args:
            events: list of Events to evaluate

        Raises:
            exceptions.InvalidEventsError: if events are overlapping
        """
        # TODO: implement
        for i, event in enumerate(events):
            end_event = event.start + event.duration
            for k, check in enumerate(events):
                end_check = check.start + check.duration
                # Exclude current event in the list.
                if i == k:
                    continue
                if check.start == event.start:
                    raise exceptions.InvalidEventsError()
                elif check.start < end_event and end_check > event.start:
                    # Do not raise an exception if events end and start at the same index.
                    if end_check == event.start:
                        continue
                    raise exceptions.InvalidEventsError()



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

        event_starts = []
        event_durations = []
        event_max = 0
        for event in self.events:
            event_starts.append(event.start)
            event_durations.append(event.duration)
            event_max += event.duration
        
        results = {
            "min": min(event_starts),
            "max": max(event_durations), 
            "percent": event_max/Timeline.size * 100
            }
        return results

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