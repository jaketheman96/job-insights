from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salaries = []
    file = read(path)
    for salary in file:
        if (
            salary["max_salary"].isnumeric()
            and salary["max_salary"] not in salaries
        ):
            salaries.append(int(salary["max_salary"]))
    return max(salaries)


def get_min_salary(path: str) -> int:
    salaries = []
    file = read(path)
    for salary in file:
        if (
            salary["min_salary"].isnumeric()
            and salary["min_salary"] not in salaries
        ):
            salaries.append(int(salary["min_salary"]))
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min = int(job["min_salary"])
        max = int(job["max_salary"])
        salary = int(salary)
    except Exception:
        raise ValueError

    if max < min:
        raise ValueError
    return min <= salary <= max


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_filter = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filter.append(job)
        except Exception:
            pass
    return jobs_filter
