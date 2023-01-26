from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word_1 = "Python"
    word_2 = "Javascript"
    count_1 = count_ocurrences(path, word_1)
    count_2 = count_ocurrences(path, word_2)
    assert count_1 == 1639
    assert count_2 == 122
