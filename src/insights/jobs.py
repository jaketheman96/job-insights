from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        jobs_list = [job for job in csv_reader]
        return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    job_types = []
    file = read(path)
    for job in file:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    result = []
    for job in jobs:
        if job["job_type"] in job_type:
            result.append(job)
    return result
