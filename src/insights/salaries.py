from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    allJobs = read(path)
    all_max_salaries = []
    higher = 0
    for job in allJobs:
        job_max = job["max_salary"]
        if job_max != '' and job_max != 'invalid':
            all_max_salaries.append(job_max)
    for max in all_max_salaries:
        max_number = int(max)
        if max_number > higher:
            higher = max_number
    print(higher)
    return higher


def get_min_salary(path: str) -> int:
    all_jobs = read(path)
    all_min_salaries = []
    lower = get_max_salary(path)
    for job in all_jobs:
        job_max = job["min_salary"]
        if job_max != '' and job_max != 'invalid':
            all_min_salaries.append(job_max)
    for min in all_min_salaries:
        min_number = int(min)
        if min_number < lower:
            lower = min_number
    print(lower)
    return lower


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        "max_salary" not in job.keys()
        or "min_salary" not in job.keys()
        or not str(job["max_salary"]).isdigit()
        or not str(job["min_salary"]).isdigit()
        or int(job["min_salary"]) > int(job["max_salary"])
        or type(salary) not in [int, str]
      ):
        raise ValueError

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError


if __name__ == "__main__":
    myMaxMoney = get_max_salary("data/testSalary.csv")
    myMinMoney = get_min_salary("data/jobs.csv")
    salaryRange = matches_salary_range(read("data/jobs.csv")[3], 4000)
