import pytest

def calculate_distance(speed, time):
    time_in_hours = time / 60
    return speed * time_in_hours

def test_calculate_distance():
    speed = [50, 60, 70]
    time = [30, 45, 60]
    expected_distances = [25, 45, 70]
    for i in range(len(speed)):
        assert round(calculate_distance(speed[i], time[i]), 2) == expected_distances[i]

def test_calculate_distance_zero_speed():
    speed = 0
    time = 30
    assert calculate_distance(speed, time) == 0

def test_calculate_distance_zero_time():
    speed = 50
    time = 0
    assert calculate_distance(speed, time) == 0

def test_calculate_distance_negative_speed():
    speed = -50
    time = 30
    with pytest.raises(ValueError):
        calculate_distance(speed, time)

def test_calculate_distance_negative_time():
    speed = 50
    time = -30
    with pytest.raises(ValueError):
        calculate_distance(speed, time)
