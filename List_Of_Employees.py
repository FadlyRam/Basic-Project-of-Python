class Employees:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


# Sample job data
jobMachineLearning = {
    "Job": "Machine Learning Engineer",
    "Salary": 97.090,
}
jobDataScience = {
    "Job": "Data Science And Analytics",
    "Salary": 96.072,
}
_jobs = [jobMachineLearning, jobDataScience]

# Sample employee data
employee = Employees("Fadly Ramdani", 19, _jobs[0])
_employees = [employee]

# Output
print("List of Employees at Future Tech\n")
for _employee in _employees:
    print(f"Name\t: {_employee.name}")
    print(f"Age\t: {_employee.age}")
    print(f"Job\t: {_employee.job['Job']}")
    print(f"Salaryy\t: ${_employee.job['Salary']}")
    print()

# If add employee and new job
option = input(f"Do you want to add emploees?\n'y' for yes and 'n' forr no\t:")

while option == "y":
    # newEmpoyee
    nameEmployee = input("New employee name\t: ")
    ageEmployee = int(input("New employee age\t: "))
    print(f"Choose a new employee jobs:")

    # List Data Jobs
    i = 0
    while i < len(_jobs):
        # Take name jobs
        job = _jobs[i]
        print(f"{i+1}\t: {job['Job']}")
        i += 1
    print("0\t: New Job")
    optionJob = int(input("Choice\t: "))

    # Add New Job to List _jobs
    if optionJob == 0:
        newJob = input("New job name\t: ")
        salaryNewJob = float(input(f"{newJob} salary\t:$"))
        _jobs.append({"Job": newJob, "Salary": salaryNewJob})

        # Add New Employee to List _employees
        _employees.append(Employees(nameEmployee, ageEmployee, _jobs[-1]))
    else:
        # Add New Employee to List .append
        _employees.append(
            Employees(nameEmployee, ageEmployee, _jobs[optionJob-1]))

    print("\nList of Employees at Future Tech\n")
    for _employee in _employees:
        print(f"Name\t: {_employee.name}")
        print(f"Age\t: {_employee.age}")
        print(f"Job\t: {_employee.job['Job']}")
        print(f"Salaryy\t: ${_employee.job['Salary']}")
        print()
    option = input(
        f"Do you want to add emploees?\n'y' for yes and 'n' forr no\t:")

# END
print("Thank You")
