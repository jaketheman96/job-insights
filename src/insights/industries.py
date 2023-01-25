from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industries = []
    file = read(path)
    for industry in file:
        if (
            industry["industry"] not in industries
            and industry["industry"] != ""
        ):
            industries.append(industry["industry"])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    result = []
    for job in jobs:
        if job["industry"] in industry:
            result.append(job)
    return result
