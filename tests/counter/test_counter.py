from src.pre_built.counter import count_ocurrences
# Python = 1639
# JS = 122
path = "data/jobs.csv"
wordPython = "Python"
wordJS = "Javascript"


def test_counter():
    python_ocurrences = count_ocurrences(path, wordPython)
    js_ocurrences = count_ocurrences(path, wordJS)
    assert python_ocurrences == 1639
    assert js_ocurrences == 122
