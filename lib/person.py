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
    def __init__ (self,name,job):
        if  len(name) <= 25:
            self.name = name
            
        else:
            print ("Name must be string under 25 characters.")

        if job in APPROVED_JOBS:
            self.job = job
        else:
            print(("The job must be in the following list of jobs:"))

kim = Person("kim","Sales")

   
