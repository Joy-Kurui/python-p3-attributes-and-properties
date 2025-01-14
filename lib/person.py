#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        self._name = name
        self._job = job
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
         if isinstance(name, str) and 1 <= len(name) <= 25:
           self._name = name.title() 
         else:
            print("Name must be string under 25 characters.")
    @property
    def job(self):
        return self._job
    @job.setter
    def job(self, job):
        if job in self.APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
    


    