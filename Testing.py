class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч.; ' 
                f'Дистанция: {self.distance:.3f} км; ' 
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}. ')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65  # The distance that an athlete covers in one step 
    M_IN_KM = 1000  # Constant, how many kilometers to meters

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        # преодолённая_дистанция_за_тренировку / время_тренировки 
        mean_speed = self.get_distance()/self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info = InfoMessage(self.action, self.duration, self.get_distance(),
                           self.get_mean_speed(), self.get_spent_calories())
        print(info.get_message())


class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79 

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
        self.duration = duration*60
    
    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()

    def get_spent_calories(self) -> float:
        spent_calories = (
            (self.CALORIES_MEAN_SPEED_MULTIPLIER * 
             self.get_mean_speed() + 
             self.CALORIES_MEAN_SPEED_SHIFT) * self.weight / 
            self.M_IN_KM * self.duration) 
        
        return spent_calories


class SportsWalking(Training):

    """Тренировка: спортивная ходьба."""
    CALORIES_FIRST_CONSTANT = 0.035
    CALORIES_SECOND_CONSTANT = 0.029
    
    def __init__(self, action: int, duration: float, weight: float, height) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        self.duration = duration*60
    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()

    def get_spent_calories(self) -> float:
        spent_calories = (
        (self.CALORIES_FIRST_CONSTANT * 
        self.weight + 
        (self.get_mean_speed()**2 / self.height) * 
        self.CALORIES_SECOND_CONSTANT * self.weight) * 
        self.duration)  

        return spent_calories

class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38 #The distance that an athlete covers in one row
    CALORIES_FIRST_CONSTANT = 1.1
    CALORIES_SECOND_CONSTAN = 2

    def __init__(self, action: int, duration: float, weight: float, length_pool, count_pool) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.duration = duration*60
    
    def get_distance(self) -> float:
        return super().get_distance()
    
    def get_mean_speed(self) -> float:
        mean_speed = self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        spent_calories = (
        self.get_mean_speed() + self.CALORIES_FIRST_CONSTANT) * self.CALORIES_SECOND_CONSTAN * self.weight * self.duration

        return spent_calories

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_list = {'SWM':Swimming,
                    'RUN':Running,
                    'WLK':SportsWalking}
    select_training = training_list[workout_type](*data)
    return select_training


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    return info


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]), # action, duration (in h), weight, lenght_pool, count_pool
        ('RUN', [15000, 1, 75]), # action, duration (in h), weight
        ('WLK', [9000, 1, 75, 180]), # action, duration (in h), weight, height
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

