from datetime import time


class Quest:

    def __init__(self, name, description, goal) -> None:
        # Create a __init__ method
        # Describe class propeties (свойства) 
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def accept_quest(self):
        if self.pass_quest() is not None:
            self.start_time = time.now()
            print(f'Начало "{self.name}" положено')
            return self.start_time
        else:
            print('С этим испытанием вы уже справились')

    def pass_quest(self):
        if self.accept_quest() != None:
            end_time = time.now()
            completion_time = end_time - accept_quest()
            print(f'Квест "{Quest.name}" окончен.' 
                  f'Время выполнения квеста: {completion_time}')
            return end_time
        else:
            print('Нельзя завершить то, что не имеет начала!')


# arguments for created variable
quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

# create a variable 'new_quest'
new_quest = Quest(quest_name, quest_description, quest_goal) 

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())
