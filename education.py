"""This program is designed to read, process and output training data."""

from dataclasses import dataclass, asdict

@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: str
    distance: str
    speed: str
    calories: str

    def get_message(self) -> str:
        """Выводим информацию о тренировке."""
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')

@dataclass
class Training:
    """Базовый класс тренировки."""

    LEN_STEP = 0.65  # Расстояние, которое спортсмен преодолевает за один шаг.
    M_IN_KM = 1000  # Постоянная, сколько километров до метров.
    HOURS_TO_MINUTS = 60
    action: int
    duration: float
    weight: float

    def get_distance(self) -> float:
        """Возвращает дистанцию (в километрах)."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Возвращает значение средней скорости."""
        return self.get_distance() / self.duration

    def get_spent_calories(self):
        """Возвращает количество израсходованных килокалорий."""
        return

    def show_training_info(self) -> InfoMessage:
        """Возвращает объект класса сообщения.

        Returns:
            InfoMessage: информация о результатах
                         тренировки из класса InfoMessage.
        """
        return InfoMessage(self.__class__.__name__,
                           self.duration, self.get_distance(),
                           self.get_mean_speed(), self.get_spent_calories())

@dataclass
class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    action: int
    duration: float
    weight: float

    def get_spent_calories(self) -> float:
        """Возвращает количество израсходованных килокалорий.

        Длительность тренировки переведена в минуты.
        """
        duration = self.duration * self.HOURS_TO_MINUTS
        return (
               (self.CALORIES_MEAN_SPEED_MULTIPLIER
                * self.get_mean_speed()
                + self.CALORIES_MEAN_SPEED_SHIFT)
            * self.weight / self.M_IN_KM * duration)

@dataclass
class SportsWalking(Training):
    """Тренировка: Спортивная ходьба."""

    CALORIES_FIRST_CONSTANT = 0.035
    CALORIES_SECOND_CONSTANT = 0.029
    KMH_TO_MS = 0.278
    SM_TO_M = 100

    action: int
    duration: float
    weight: float
    height: float

    def get_spent_calories(self) -> float:
        """Возвращает количество израсходованных килокалорий.

        Длительность (duration) тренировки переведена в минуты.

        Средняя скорость (mean_speed) тренировки переведена из км/ч в м/c
        """
        duration = self.duration * self.HOURS_TO_MINUTS
        mean_speed = self.get_mean_speed() * self.KMH_TO_MS
        self.height = self.height/self.SM_TO_M
        return (
               (self.CALORIES_FIRST_CONSTANT * self.weight
                + (mean_speed**2 / self.height)
                * self.CALORIES_SECOND_CONSTANT
                * self.weight)
            * duration)

@dataclass
class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38  # Расстояние, к-е спортсмен преодолевает за один гребок
    CALORIES_FIRST_CONSTANT = 1.1
    CALORIES_SECOND_CONSTAN = 2

    action: int
    duration: float
    weight: float
    length_pool: int
    count_pool: int


    def get_mean_speed(self) -> float:
        """Возвращает значение средней скорости движения."""
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Возвращает количество израсходованных килокалорий."""
        return ((self.get_mean_speed()
                + self.CALORIES_FIRST_CONSTANT)
                * self.CALORIES_SECOND_CONSTAN * self.weight
                * self.duration
                )


def read_package(workout_type: str, data: list) -> Training:
    """Функция чтения принятых пакетов.

    Функция принимает кортеж, в который входят:

    Args:
        workout_type (str): в виде аббривиатур тренировок
        data (list): в виде значений тренировок, совершенных пользователем.

    Например: ('SWM', [720, 1, 80, 25, 40])

    Словарь training_list соотносит аббривиатуру тренировки
    с классом в коде и функция возвращает значение в виде:

    Класс(*Список значений тренировок, соответствующий классу)

    Например:

    Swimming(100, 200, ...)

    """
    training_list = {'SWM': Swimming,
                     'RUN': Running,
                     'WLK': SportsWalking}
    return training_list[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
