from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    allJobs = read(path)
    all_unique_industries = []
    for job in allJobs:
        job_ind = job["industry"]
        if job_ind not in all_unique_industries and job_ind != '':
            all_unique_industries.append(job_ind)
    print(all_unique_industries)
    return all_unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError


if __name__ == "__main__":
    myIndustry = get_unique_industries("data/jobs.csv")
