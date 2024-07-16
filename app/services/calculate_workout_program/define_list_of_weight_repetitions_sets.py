def define_list_of_weight(start_weight: float, purpose_weight: float) -> list[float]:

    start_weight *= 0.75
    step = int((purpose_weight - start_weight) / 2.5)
    return [start_weight + 2.5 * x for x in range(step)]


def define_list_of_repetitions(repetitions: int, desired_result: str) -> list[int]:

    match desired_result:
        case 'похудение с поддержанием физ. формы':
            min_repetition_or_sets = int(round(repetitions * 0.9, 0))
            max_repetition_or_sets = int(round(repetitions * 1.6, 0))
        case 'поддержание физ. формы':
            min_repetition_or_sets = int(round(repetitions * 0.9, 0))
            max_repetition_or_sets = int(round(repetitions * 1.1, 0))
        case 'набор мышечной массы':
            min_repetition_or_sets = int(round(repetitions * 0.5, 0))
            max_repetition_or_sets = int(round(repetitions * 1, 0))
        case _:
            min_repetition_or_sets = max_repetition_or_sets = repetitions

    return [x for x in range(min_repetition_or_sets, max_repetition_or_sets+1)]


def define_list_of_sets(sets: int) -> list[int]:

    min_repetition_or_sets = int(round(sets * 0.6, 0))
    max_repetition_or_sets = int(round(sets * 1.4, 0))

    return [x for x in range(min_repetition_or_sets, max_repetition_or_sets+1)]