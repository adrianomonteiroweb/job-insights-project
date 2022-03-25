from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobsList = list(reader)
        return jobsList

# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/

# https://www.codegrepper.com/code-examples/python/spamreader+%3D+csv.reader%28csvfile%2C+delimiter%3D%27+%27%2C+quotechar%3D%27%7C%27%29
