from src.jobs import read


def get_unique_job_types(path):

    unique_jobs = set()

    for job in read(path):
        unique_jobs.add(job["job_type"])
    return unique_jobs

# https://www.javatpoint.com/python-set-function
# https://www.w3schools.com/python/ref_set_add.asp
# https://www.tutorialspoint.com/python/file_read.htm


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


# retorna array usando repetição for/in
# com condicionar da coluna de tipo
# por tipo selecionado


def get_unique_industries(path):
    unique_industries = set()

    for job in read(path):
        if job["industry"] != "":
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    salaries = set()

    for salary in read(path):
        if salary["max_salary"].isnumeric():
            salaries.add(int(salary["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    salaries = set()

    for salary in read(path):
        if salary["min_salary"].isnumeric():
            salaries.add(int(salary["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    salary_exists = "min_salary" in job and "max_salary" in job

    salary_number = (
        salary_exists
        and isinstance(job["min_salary"], int)
        and isinstance(job["max_salary"], int)
    )

    salary_is_number = isinstance(salary, int)

    minimum_wage_above_maximum = (
        salary_number
        and job["min_salary"] > job["max_salary"]
    )

    salary_range = (
        salary_number
        and salary_is_number
        and job["min_salary"] <= salary <= job["max_salary"]
    )

    if salary_range:
        return True
    elif (
        not salary_exists
        or not salary_number
        or not salary_is_number
        or minimum_wage_above_maximum
    ):
        raise ValueError("The values of your inputs must be of type integer.")
    else:
        return False

# https://www.w3schools.com/python/ref_func_isinstance.asp
# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
    return filtered_jobs
