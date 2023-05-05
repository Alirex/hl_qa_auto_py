"""
В программе есть списки тестировщиков (имена, айдишники), которые:
- могут писать тест дизайны
- могут писать тест скрипты
- могут ревьюить скрипты
- сегодня не на работе

Любой тестировщик может входить в одну или несколько групп.


Создать списки:
- всех тестировщиков в команде
- тестировщиков, которые могут только писать скрипты
- тестировщиков, которые сегодня на работе
- тестировщиков, которые могут писать и ревьюить скрипты, и которые сегодня на работе


Полученные списки вывести в отсортированном виде.


test_design_writers = [1, 3, 5]
scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]


всех тестировщиков в команде
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

могут писать только тест скрипты
[4, 6, 7, 8]

тестировщиков, которые сегодня на работе
[3, 4, 7, 8, 9, 10]

тестировщиков, которые могут писать и ревьюить скрипты, и которые сегодня на работе
[3]
"""
from typing import TypeAlias, NamedTuple

T_TESTER: TypeAlias = int
T_TESTERS: TypeAlias = list[T_TESTER]


class ResultGroups(NamedTuple):
    testers_all: T_TESTERS
    scripters_only: T_TESTERS
    in_office: T_TESTERS
    testers_that__write_test_script__make_review__in_office: T_TESTERS


def normalize(value: set[T_TESTER]) -> T_TESTERS:
    return sorted(value)


def arrange_testers(
    test_design_writers: T_TESTERS,
    scripters: T_TESTERS,
    reviewers: T_TESTERS,
    out_of_office_today: T_TESTERS,
) -> ResultGroups:
    test_design_writers__as_set = set(test_design_writers)
    scripters__as_set = set(scripters)
    reviewers__as_set = set(reviewers)

    out_of_office_today__as_set = set(out_of_office_today)

    testers_all = test_design_writers__as_set.union(scripters__as_set).union(
        reviewers__as_set
    )

    scripters_only = scripters__as_set - test_design_writers__as_set - reviewers__as_set

    in_office = testers_all - out_of_office_today__as_set

    testers_that__write_test_script__make_review__in_office = (
        scripters__as_set.intersection(reviewers__as_set).intersection(in_office)
    )

    return ResultGroups(
        testers_all=normalize(testers_all),
        scripters_only=normalize(scripters_only),
        in_office=normalize(in_office),
        testers_that__write_test_script__make_review__in_office=normalize(
            testers_that__write_test_script__make_review__in_office
        ),
    )


def main() -> None:
    test_design_writers = [1, 3, 5]
    scripters = [2, 3, 4, 6, 7, 8]
    reviewers = [1, 2, 3, 9, 10]
    out_of_office_today = [2, 5, 6, 1]

    result_groups = arrange_testers(
        test_design_writers=test_design_writers,
        scripters=scripters,
        reviewers=reviewers,
        out_of_office_today=out_of_office_today,
    )

    for key, value in result_groups._asdict().items():
        print(f"{key.replace('_', ' ').capitalize()}:")
        print(value)
        print()


if __name__ == "__main__":
    main()
