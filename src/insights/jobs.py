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
            # print(pathList)
    except FileNotFoundError as err:
        print("Arquivo não encontrado!")
        print(err)
    return pathList

    # raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    allJobs = read(path)
    allUniqueJobs = []
    for job in allJobs:
        jobType = job['job_type']
        if jobType not in allUniqueJobs:
            allUniqueJobs.append(jobType)
    print(allUniqueJobs)
    return allUniqueJobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    print(filtered_jobs)
    return filtered_jobs


if __name__ == "__main__":
    myJobs = read("data/jobs.csv")
    myUnique = get_unique_job_types("data/jobs.csv")
    myFiltered = filter_by_job_type(myJobs, "INTERN")
