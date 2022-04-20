import pytest
from timeline import Timeline
from event import Event
import exceptions

@pytest.mark.parametrize(
    "events",
    [
        # TODO: add tests for edge cases
    ],
)
def test_invalid_events(events):
    with pytest.raises(exceptions.InvalidEventsError):
        Timeline(events=events)


@pytest.mark.parametrize(
    "start, duration",
    [
        # TODO: add tests for edge cases
    ],
)
def test_out_of_bounds(start, duration):
    with pytest.raises(exceptions.EventOutOfBoundsError):
        Timeline(events=[Event(start=start, duration=duration)])


@pytest.mark.parametrize(
    "events, expected",
    [
        # TODO: add tests for edge cases
    ],
)
def test_get_duration_stats(events, expected):
    assert expected == Timeline(events=events).get_duration_stats()
