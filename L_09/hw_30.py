"""
Занятия проходят по понедельникам и четвергам в 19:15
Первое занятие произошло 27.03.2023.
Вывести список всех занятий в таком формате (номера лекций выровнены по правому краю):


Lecture  1: 27 Mar 2023 19:15
Lecture  2: 30 Mar 2023 19:15
Lecture  3: 03 Apr 2023 19:15
...
Lecture  9: 24 Apr 2023 19:15
Lecture 10: 27 Apr 2023 19:15
...
Lecture 32: 13 Jul 2023 19:15
"""
import datetime
import enum
from itertools import cycle
from typing import TypeAlias, NamedTuple
from collections.abc import Iterable


class LessonSchedule(NamedTuple):
    number: int
    date: datetime.date
    time: datetime.time


T_LESSON_SCHEDULES: TypeAlias = list[LessonSchedule]


@enum.unique
class DayOfWeek(enum.IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    @staticmethod
    def get_amount_of_days_to_next_day_of_week(
        current_day_of_week: "DayOfWeek",
        next_day_of_week: "DayOfWeek",
        #
        is_same_week: bool = False,
    ) -> int:
        amount_of_days_total = len(DayOfWeek)
        if current_day_of_week == next_day_of_week:
            return 0 if is_same_week else amount_of_days_total

        if next_day_of_week < current_day_of_week:
            next_day_of_week += amount_of_days_total

        return (next_day_of_week - current_day_of_week) % amount_of_days_total


# TODO ? Implement schedule for different time of lesson start?
#   Use NamedTuple with fields: day_of_week, time.

# TODO ? Add skipped (holidays,etc) and forced(moved to some date and time) lessons?


def get_schedule(
    start_date: datetime.date,
    #
    amount_of_lessons: int = 32,
    time_of_lesson_start: datetime.time = datetime.time(19, 15),
    days_of_week: Iterable[DayOfWeek, ...] = (
        DayOfWeek.MONDAY,
        DayOfWeek.THURSDAY,
    ),
) -> T_LESSON_SCHEDULES:
    result = []

    days_of_week_cycle = cycle(days_of_week)

    current_date = start_date
    current_time = time_of_lesson_start
    current_day_of_week = current_date.weekday()

    # Get current day of week from cycle.
    current_day_of_week_from_cycle = next(days_of_week_cycle)
    while current_day_of_week != current_day_of_week_from_cycle:
        current_day_of_week_from_cycle = next(days_of_week_cycle)

    current_lesson_number = 1

    while True:
        result.append(
            LessonSchedule(
                number=current_lesson_number, date=current_date, time=current_time
            )
        )

        current_lesson_number += 1
        if current_lesson_number > amount_of_lessons:
            break

        # Get next day of week from cycle.
        previous_day_of_week_from_cycle = current_day_of_week_from_cycle
        current_day_of_week_from_cycle = next(days_of_week_cycle)

        # Get amount of days to next day of week.
        amount_of_days_to_next_day_of_week = (
            DayOfWeek.get_amount_of_days_to_next_day_of_week(
                current_day_of_week=previous_day_of_week_from_cycle,
                next_day_of_week=current_day_of_week_from_cycle,
            )
        )

        # Get next date.
        current_date += datetime.timedelta(days=amount_of_days_to_next_day_of_week)

    return result


def print_schedule(schedule: T_LESSON_SCHEDULES, is_with_weekday: bool = False) -> None:
    for lesson in schedule:
        message_as_list = [
            f"Lecture {lesson.number:2}: {lesson.date.strftime('%d %b %Y')} {lesson.time.strftime('%H:%M')}"
        ]
        if is_with_weekday:
            message_as_list.append(lesson.date.strftime("%A"))

        print(*message_as_list)


def main() -> None:
    # 27 Mar 2023
    start_date = datetime.date(year=2023, month=3, day=27)

    schedule = get_schedule(
        start_date=start_date,
    )

    print_schedule(
        schedule=schedule,
        # is_with_weekday=True,
    )

    # 13 Jul 2023
    control_end_date = datetime.date(year=2023, month=7, day=13)

    # noinspection Assert
    assert (
        schedule[-1].date == control_end_date
    ), f"{schedule[-1].date=}, {control_end_date=}"


if __name__ == "__main__":
    main()
