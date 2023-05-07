"""
Создать два класса, предметную область выбрать по своему желанию.

Классы должны содержать:
- минимум два поля экземпляров и одно поле класса
- минимум два метода экземпляра

Хотя бы в одном классе:
- минимум один метод класса
- минимум один статический метод

К методам добавить строки документации.


Методы должные быть НЕ get/set поле, а что-то оригинальнее:) (но если надо их, тоже можно добавить)
Написать код который создает несколько экземпляров и взаимодействует с объектами
Задание в том числе и на фантазию


Как пример, классы Employee (сотрудник) и Company (компания).
"""
import logging
import queue
import random
import uuid
import weakref
from dataclasses import dataclass, field
from typing import ClassVar, Optional, Final, NamedTuple

from faker import Faker


@dataclass
class Task:
    """Task.
    Some task need to be solved.
    Complexity is the amount of power needed to solve task.
    """

    name: str
    complexity: int = field(default_factory=lambda: random.randint(1, 100))

    TASKS_QUEUE: ClassVar[queue.Queue["Task"]] = queue.Queue()
    TASKS_SOLVED_TOTAL: ClassVar[int] = 0

    def __post_init__(self) -> None:
        entity_name = self.__class__.__name__
        self._logger = logging.getLogger(f"{entity_name}:{self.name}")
        self._logger.info("created")

    def solve_and_say_is_solved(self, power: int) -> bool:
        """Solve task"""
        self.complexity -= power

        if self.complexity <= 0:
            self._logger.info("solved")
            self.increase_tasks_solved_total()
            return True
        return False

    @classmethod
    def increase_tasks_solved_total(cls) -> None:
        """Increase tasks solved total"""
        cls.TASKS_SOLVED_TOTAL += 1

    @classmethod
    def create_some_tasks(cls, modifier: int):
        for _ in range(random.randint(0, modifier)):
            cls.TASKS_QUEUE.put(Task(Faker().name()))


@dataclass
class Worker:
    """Worker.
    Can solve tasks using power.
    One worker can solve only one task at a time.
    Obtain boost to power after solving task.
    """

    name: str
    power: int = field(default_factory=lambda: random.randint(1, 100))
    internal_id: uuid.UUID = field(default_factory=uuid.uuid4)

    task: Task | None = None

    SPEED_MULTIPLIER: Final[int] = 2
    MINIMUM_WORKERS: Final[int] = 1

    POWER_USED_TOTAL: ClassVar[int] = 0

    ALL_WORKERS: ClassVar[set["Worker"]] = set()

    def __post_init__(self) -> None:
        entity_name = self.__class__.__name__
        self._logger = logging.getLogger(f"{entity_name}:{self.name}")
        self._logger.info("created")

        self.ALL_WORKERS.add(self)

    def __hash__(self) -> int:
        return int(self.internal_id.hex, base=16)

    def make_work_and_say_is_idle(self) -> bool:
        """Make work"""

        power_for_round = self.power * self.SPEED_MULTIPLIER
        while power_for_round:
            if self.task is None:
                task = self.get_task()
                if task is None:
                    self._logger.info("is idle")
                    return True
                else:
                    self.task = task

            task = self.task
            provided_power = min(power_for_round, task.complexity)
            power_for_round -= provided_power
            if task.solve_and_say_is_solved(power=provided_power):
                self._logger.info("solved {task.name}")
                self.task = None
                self.add_used_power(power=provided_power)

                # Boost power
                self.power += 1
            else:
                self._logger.info(
                    "solving {task.name}. complexity remains: {task.complexity}"
                )
        return False

    @classmethod
    def spawn_worker(cls, name: str | None = None) -> "Worker":
        """Spawn worker"""
        if name is None:
            name = Faker().name()
        return cls(name)

    def self_destruct(self) -> None:
        """Self destruct"""
        self.ALL_WORKERS.remove(self)
        self._logger.info("self destructed")
        del self

    @staticmethod
    def get_task() -> Optional["Task"]:
        """Get task"""
        try:
            return Task.TASKS_QUEUE.get(block=False)
        except queue.Empty:
            return None

    @classmethod
    def add_used_power(cls, power: int) -> None:
        """Add used power"""
        cls.POWER_USED_TOTAL += power


class Stats(NamedTuple):
    """Stats.
    Some stats about current state.
    """

    workers_active: int
    power_used_total: int
    tasks_in_progress: int
    tasks_left: int
    tasks_solved_total: int


def main() -> None:
    # noinspection PyPep8Naming
    MAX_LOAD: Final[int] = 100

    for _ in range(Worker.MINIMUM_WORKERS):
        Worker.spawn_worker()

    Task.create_some_tasks(modifier=10)

    logger = logging.getLogger("main")

    stats: list[Stats] = []

    ticks_left = 20
    while ticks_left:
        logger.info("=" * 10)
        logger.info(f"ticks left: {ticks_left}")

        # [generate_extra_tasks]-[BEGIN]
        if random.randint(0, 1):
            Task.create_some_tasks(
                random.randint(0, MAX_LOAD - Task.TASKS_QUEUE.qsize())
            )
        # [generate_extra_tasks]-[END]

        # [make_work]-[BEGIN]
        idle_workers = weakref.WeakSet()
        for worker in Worker.ALL_WORKERS:
            if worker.make_work_and_say_is_idle():
                idle_workers.add(worker)
        # [make_work]-[END]

        # [load_balancer]-[BEGIN]
        # Slowly react to load changes.
        # If there idle workers, kill one of them. (if there are more than minimum workers)
        # If there are too many tasks in queue, spawn new worker.
        if len(idle_workers) and len(Worker.ALL_WORKERS) > Worker.MINIMUM_WORKERS:
            idle_workers.pop().self_destruct()

        if not Task.TASKS_QUEUE.empty():
            Worker.spawn_worker()
        # [load_balancer]-[END]

        ticks_left -= 1

        stats_item = Stats(
            workers_active=len(Worker.ALL_WORKERS),
            power_used_total=Worker.POWER_USED_TOTAL,
            tasks_in_progress=len(
                list(filter(lambda x: x.task is not None, Worker.ALL_WORKERS))
            ),
            tasks_left=Task.TASKS_QUEUE.qsize(),
            tasks_solved_total=Task.TASKS_SOLVED_TOTAL,
        )
        stats.append(stats_item)

        logger.info(f"stats: {stats_item}")

    print("stats:")
    for stats_item in stats:
        print(stats_item)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
