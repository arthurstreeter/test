import pytest
from timeline import Timeline
from event import Event
import exceptions

@pytest.mark.parametrize(
    "events",
    [
        # TODO: add tests for edge cases
        pytest.param("1,4 2,5", id="events are a string"),
        pytest.param((1,4), id="events are a tuple"),
        pytest.param(([1,4],[2,5]), id="events are a tuple of lists"),
        pytest.param({1:[0,4],2:[5,10]}, id="events are a dict"),
        pytest.param([Event(1,3),Event(1,4),Event(1,5)], id="events start at the same time"),
        pytest.param([Event(1,3),Event(2,4),Event(3,5)], id="events overlap")
    ],
)
def test_invalid_events(events):
    with pytest.raises(exceptions.InvalidEventsError):
        Timeline(events=events)


@pytest.mark.parametrize(
    "start, duration",
    [
        pytest.param(21,1, id="event's start is beyond Timeline.size"),
        pytest.param(1,50, id="event's duration is longer than Timeline.size"),
    ],
)
def test_out_of_bounds(start, duration):
    with pytest.raises(exceptions.EventOutOfBoundsError):
        Timeline(events=[Event(start=start, duration=duration)])


@pytest.mark.parametrize(
    "events, expected",
    [
        # TODO: add tests for edge cases
        pytest.param([Event(0,4),Event(4,1),Event(5,5)], {"min":0,"max":5,"percent":.5}, id="events are next to eachother"),
        pytest.param([Event(9,1),Event(13,2),Event(16,3)], {"min":9,"max":3,"percent":.3}, id="events are spaced out"),
    ],
)
def test_get_duration_stats(events, expected):
    assert expected == Timeline(events=events).get_duration_stats()
