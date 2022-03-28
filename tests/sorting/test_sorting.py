import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 2400, "min_salary": 1200, "date_posted": "2010-01-01"},
        {"max_salary": 3600, "min_salary": 2600, "date_posted": "2020-01-01"},
        {"max_salary": 5000, "min_salary": 3700, "date_posted": "2022-01-01"},
    ]

    expect = [
        [jobs[0], jobs[1], jobs[2]],
        [jobs[2], jobs[1], jobs[0]],
        [jobs[2], jobs[1], jobs[0]],
    ]

    sort_by(jobs, "min_salary")
    assert jobs == expect[0]
    sort_by(jobs, "max_salary")
    assert jobs == expect[1]
    sort_by(jobs, "date_posted")
    assert jobs == expect[2]
    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")
