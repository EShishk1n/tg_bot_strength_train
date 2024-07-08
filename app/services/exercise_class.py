class Exercise:
    def __init__(self, exercise: str):
        self.weight = int(exercise.split('*')[0])
        self.repetitions = int(exercise.split('*')[1])
        self.sets = int(exercise.split('*')[2])

    def calculate_current_exercise_weight(self) -> float:
        """Считает суммарный вес упражнения (вес*повторения*подходы)"""
        return self.weight * self.repetitions * self.sets


class PurposeExercise(Exercise):
    def __init__(self, exercise: str):
        super().__init__(exercise[:-2])
        self.frequency = int(exercise[-1:])
