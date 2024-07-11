import datetime
import random

from app.services.define_list_of_exercise_weight import main
from app.services.define_list_of_weight_repetitions_sets import define_list_of_weight, define_list_of_repetitions, \
    define_list_of_sets
from app.services.exercise_class import Exercise, PurposeExercise


class WorkoutProgramCalculation:
    def __init__(self, current_exercise: Exercise, purpose_exercise: PurposeExercise,
                 date_reached_at_plan: datetime.date, desired_result: str):
        self.current_exercise = current_exercise
        self.purpose_exercise = purpose_exercise
        self.date_reached_at_plan = date_reached_at_plan
        self.list_of_exercise_weight = main(self.current_exercise, self.purpose_exercise, self.date_reached_at_plan)
        self.list_of_weight = define_list_of_weight(self.current_exercise.weight, self.purpose_exercise.weight)
        self.list_of_repetitions = define_list_of_repetitions(self.purpose_exercise.repetitions, desired_result)
        self.list_of_sets = define_list_of_sets(self.purpose_exercise.sets)

    def calculate_workout_program(self) -> list:

        workout_program = []
        for exercise_weight in self.list_of_exercise_weight:
            better_ways_to_reach_exercise_weight = self.choose_better_ways_to_reach_exercise_weight(exercise_weight)
            random_way_to_reach_exercise_weight = self.choose_random_way_to_reach_exercise_weight(
                better_ways_to_reach_exercise_weight)
            workout_program.append(random_way_to_reach_exercise_weight)
        workout_program[
            0] = f'{self.current_exercise.weight}*{self.current_exercise.repetitions}*{self.current_exercise.sets}'
        workout_program[
            -1] = f'{self.purpose_exercise.weight}*{self.purpose_exercise.repetitions}*{self.purpose_exercise.sets}'

        return workout_program

    @staticmethod
    def choose_random_way_to_reach_exercise_weight(list_of_ways: list) -> str:
        """Из лучших вариантов выбирает рандомно один"""

        return random.choice(list_of_ways)

    def choose_better_ways_to_reach_exercise_weight(self, target: int) -> list:
        """Выбирает лучшие варианты достижения суммарного веса.
        Например, за тренировку нужно достичь 2880 кг; лучшие варианты (вес соответствует весам в list_of_weight):
        90*8*4, 80*9*4, 60*12*4, 45*16*4, 90*16*2, 80*12*3, 60*16*3"""

        all_possible_ways_to_reach_exercise_weight = self.find_all_possible_ways_to_reach_exercise_weight(target)
        all_possible_ways_with_delta = self.find_delta_of_weight_in_ways_with_list_of_weight(
            all_possible_ways_to_reach_exercise_weight)
        min_delta = self.find_min_delta(all_possible_ways_with_delta)

        res = self.find_items_with_min_delta(min_delta=min_delta, sup_dict=all_possible_ways_with_delta)

        return res

    def find_all_possible_ways_to_reach_exercise_weight(self, target: int) -> dict:
        """Находит все возможные варианты достижения суммарного веса."""

        suppport_dict = {}
        for repetition in self.list_of_repetitions:
            for set_ in self.list_of_sets:
                suppport_dict[f'{repetition}*{set_}'] = target / (repetition * set_)

        return suppport_dict

    def find_delta_of_weight_in_ways_with_list_of_weight(self, sup_dict: dict):
        """Добавляет ко всем возможным вариантам достижения суммарного веса разницу
        (предложенный вес - вес в списке list_of_weight)"""

        support_dict = {}
        for key, value in sup_dict.items():
            # Для каждого значения value находим минимальную разницу с ближайшим значением в списке доступных весов
            min_delta = abs(self.find_nearest(value, self.list_of_weight) - value)
            support_dict[f'{key}*{min_delta}'] = value
        return support_dict

    @staticmethod
    def find_nearest(target, spisok: list):
        nearest_item = spisok[0]
        delta = abs(spisok[0] - target)
        for item in spisok[1:]:
            if abs(target - item) < delta:
                delta = abs(target - item)
                nearest_item = item

        return nearest_item

    @staticmethod
    def find_items_with_min_delta(min_delta: float, sup_dict: dict):
        """Из всех возможных вариантов находим варианты с минимальной дельтой и оставляем только их """

        res = []
        for key, value in sup_dict.items():
            if float(key.split('*')[2]) == min_delta:
                value_new = round(value / 2.5) * 2.5
                res.append(f'{value_new}*{key.split("*")[0]}*{key.split("*")[1]}')
        return res

    @staticmethod
    def find_min_delta(sup_dict: dict):
        """Находим минимальную дельту во всем списке"""

        min_delta = float(list(sup_dict.keys())[0].split('*')[2])
        for keys in sup_dict.keys():
            delta = float(keys.split('*')[2])
            if delta < min_delta:
                min_delta = delta

        return min_delta

#
# workout = WorkoutProgramCalculation(current_exercise=Exercise('60*12*3'),
#                                     purpose_exerciuse=PurposeExercise('90*12*3*1'),
#                                     date_reached_at_plan=datetime.datetime(2024, 11, 1),
#                                     desired_result='поддержанием физ. формы')
#
# print(workout.calculate_workout_program())
