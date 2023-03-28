from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    pathList = []
    try:
        with open(path) as pathFile:
            newJobs = list(csv.DictReader(pathFile))
            pathList = newJobs
            print(pathList)
    except FileNotFoundError as err:
        print("Arquivo não encontrado!")
        print(err)
    return pathList

    # raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError


if __name__ == "__main__":
    read("data/nomes.csv")
