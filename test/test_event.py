import pytest
from event import Event


# We use pytest.mark.parametrize to pass in a list of test parameters into a unit test.
#   - this means each new parameter acts like a new unit test
#   - the first arg defines the name of the variable(s) that will be changed
#   - the second arg is a list of pytest.param objects defining the values of the var(s)
#   - the "id" of the pytes.param is displayed in the unit test output
#
# We've found that this helps enforce clean functional programming while also making it
# easier to quickly test edge cases without too much copy/pasting of tests!
#
# Read more here: https://docs.pytest.org/en/6.2.x/parametrize.html
@pytest.mark.parametrize(
    # the variable "start" will be changed for each pytest.param
    "start",
    [
        # the first arg here is what "start" will be in each iteration of the test
        # the "id" is the name displayed for the test in pytest
        pytest.param(None, id="start is None"),
        pytest.param(1.5, id="start is float"),
        pytest.param("bad", id="start is str"),
        pytest.param({}, id="start is dict"),
        pytest.param(-1000, id="start is much less than zero"),
        pytest.param(-1, id="start is less than zero"),
    ],
)
# the "start" arg corresponds to the first arg in each pytest.param
def test_invalid_start_error(start):
    # pytest.raises is used to assert that a specific exception is raised
    #
    # Read more here: https://docs.pytest.org/en/6.2.x/reference.html#pytest.raises
    with pytest.raises(ValueError):
        Event(start=start, duration=3)


@pytest.mark.parametrize(
    "duration",
    [
        pytest.param(None, id="duration is None"),
        pytest.param(1.5, id="duration is float"),
        pytest.param("bad", id="duration is str"),
        pytest.param({}, id="duration is dict"),
        pytest.param(-1000, id="duration is much less than zero"),
        pytest.param(0, id="duration is zero"),
    ],
)
def test_invalid_duration(duration):
    with pytest.raises(ValueError):
        Event(start=0, duration=duration)


@pytest.mark.parametrize(
    "item_a, item_b",
    [
        # TODO: add tests for edge cases
        # pytest.param(<item_a>, <item_b>, id=<test description>),
        pytest.param(None, None, id="items are None"),
        pytest.param(float, float, id="items are float"),
        pytest.param(str, str, id="items are str"),
        pytest.param(dict, dict, id="items are dict"),
    ],
)
def test_equal(item_a, item_b):
    assert item_a == item_b


@pytest.mark.parametrize(
    "item_a, item_b",
    [
        # TODO: add tests for edge cases
        # pytest.param(<item_a>, <item_b>, id=<test description>),
        pytest.param(None, int, id="items don't match"),
        pytest.param(int, float, id="items don't match"),
        pytest.param(float, str, id="items don't match"),
        pytest.param(str, dict, id="items don't match"),
        pytest.param(dict, None, id="items don't match"),
    ],
)
def test_not_equal(item_a, item_b):
    assert item_a != item_b


@pytest.mark.parametrize(
    "start_less, start_more",
    [
        # TODO: add tests for edge cases
        # pytest.param(<start_less>, <start_more>, id=<test description>),
        pytest.param(0, 1, id="events start 1 apart"),
        pytest.param(250, 500, id="events start 250 apart"),
    ],
)
def test_less_than(start_less, start_more):
    assert Event(start=start_less, duration=1) < Event(start=start_more, duration=1)


@pytest.mark.parametrize(
    "unsorted_list, expected",
    [
        # TODO: add tests for edge cases
        # pytest.param(<unsorted_list>, <expected>, id=<test description>),
        pytest.param([4,2,6,1,3,0,5], [0,1,2,3,4,5,6], id="7 items are sorted"),
    ],
)
def test_sort(unsorted_list, expected):
    unsorted_list.sort()
    assert unsorted_list == expected
