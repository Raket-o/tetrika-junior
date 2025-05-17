{'intervals': {'lesson': [1594702800, 1594706400],
               'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                         1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                         1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                         1594706524, 1594706524, 1594706579, 1594706641],
               'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
 'answer': 3577
 },
{'intervals': {'lesson': [1594692000, 1594695600],
               'pupil': [1594692033, 1594696347],
               'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
 'answer': 3565
 },

from typing import List, Tuple, Any

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },

]


def united_intervals(intervals: list[tuple]) -> list[tuple]:
    """The function combines overlapping intervals"""
    if not intervals:
        return []

    sorted_intervals = sorted(intervals)
    united = [sorted_intervals[0]]
    for current_start, current_end in sorted_intervals[1:]:
        last_merged_interval = united[-1]

        if current_start <= last_merged_interval[1]:
            united[-1] = (
                last_merged_interval[0],
                max(last_merged_interval[1], current_end),
            )
        else:
            united.append((current_start, current_end))
    return united


def intersection_intervals(interval1: tuple, interval2: tuple) -> tuple | None:
    """
    The function returns the intersection of two intervals,
    if there are no intersections it returns None.
    """
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if start > end:
        return None
    return start, end


def convert_pairs(lst) -> list[tuple[Any, Any]]:
    """
    The function returns timestamp pairs.
    """
    return [(lst[time_stamp], lst[time_stamp + 1]) for time_stamp in range(0, len(lst) - 1, 2)]


def appearance(intervals: dict[str, list[int]]) -> int:
    """
    The function receives a dictionary at intervals as
    input and returns the time of the pupil and teacher's
    presence in the lesson (in seconds)
    """
    lesson_intervals = convert_pairs(intervals.get("lesson", []))
    pupil_intervals = convert_pairs(intervals.get("pupil", []))
    tutor_intervals = convert_pairs(intervals.get("tutor", []))

    filter_pupil_intervals = [
        intersection_intervals(pupil_interval, lesson_interval)
        for pupil_interval in pupil_intervals
        for lesson_interval in lesson_intervals
        if intersection_intervals(pupil_interval, lesson_interval)
    ]
    filter_tutor_intervals = [
        intersection_intervals(tutor_interval, lesson_interval)
        for tutor_interval in tutor_intervals
        for lesson_interval in lesson_intervals
        if intersection_intervals(tutor_interval, lesson_interval)
    ]

    filter_pupil_intervals = [
        interval for interval in filter_pupil_intervals if interval is not None
    ]
    filter_tutor_intervals = [
        interval for interval in filter_tutor_intervals if interval is not None
    ]

    united_pupil_intervals = united_intervals(filter_pupil_intervals)
    united_tutor_intervals = united_intervals(filter_tutor_intervals)

    presence_time = []
    for p_interval in united_pupil_intervals:
        for t_interval in united_tutor_intervals:
            intersected_interval = intersection_intervals(p_interval, t_interval)
            if intersected_interval:
                presence_time.append(intersected_interval)

    total_presence_time = sum(end - start for start, end in presence_time)
    return total_presence_time


if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        assert (
            test_answer == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
