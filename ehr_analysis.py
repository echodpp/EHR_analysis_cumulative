from datetime import datetime
from pickle import FALSE, TRUE
import sqlite3


class Patient:
    """Patient information'"""

    def __init__(self, id: str, dob: str):
        """declare variables in the class patient"""
        self.id = id
        self.dob = datetime.fromisoformat(dob)

    @property
    def age(self) -> float:
        """return patient's age"""
        today = datetime.now()
        current_age = today - self.dob
        return current_age.days / 365.25


class Lab:
    """Patient's lab information"""

    def __init__(self, patientid: str, name: str, value: str, time: str):
        """declare variables in the class lab"""
        self.patientid = patientid
        self.name = name
        self.value = value
        self.time = datetime.fromisoformat(time)


def read_file(path_to_file: str) -> list[list[str]]:
    "read file.txt to a list line by line and split by tab\t"
    "computational complexity :0(N)"
    with open(path_to_file) as file:
        lines = file.readlines()
    data = []
    for i, line in enumerate(lines):
        if i > 0:  # N times
            data.append(line.strip("\n").split("\t"))  # O(1)
    return data


def parse_data(path_to_file: str) -> list[Lab] or list[Patient]:
    "INSERTed into a SQLite database"
    con = sqlite3.connect("new_db.db")
    c = con.cursor()
    data = []
    if path_to_file == "PatientCorePopulatedTable.txt":
        firstzip = list(zip(*read_file(path_to_file)))
        secondzip = zip(firstzip[0], firstzip[2])
        c.execute(
            """CREATE TABLE IF NOT EXISTS patient (id TEXT PRIMARY KEY,dob INTEGER)"""
        )
        c.executemany("INSERT INTO patient VALUES (?,?)", secondzip)
        for row in c.execute("SELECT * FROM patient"):
            id, dob = row
            data.append(Patient(id, dob))
    if path_to_file == "LabsCorePopulatedTable.txt":
        firstzip = list(zip(*read_file(path_to_file)))
        secondzip = zip(firstzip[0], firstzip[2], firstzip[3], firstzip[5])
        c.execute(
            """CREATE TABLE IF NOT EXISTS lab (patientid TEXT,name TEXT,value TEXT,dot INTEGER)"""
        )
        c.executemany("INSERT INTO lab VALUES (?,?,?,?)", secondzip)
        for row in c.execute("SELECT * FROM lab"):
            patientid, name, value, time = row
            data.append(Lab(patientid, name, value, time))
    con.commit()
    con.close()
    return data


def num_older_than(age_over: int, data: list[Patient]) -> int:
    """Calculate number of patients older than a given age"
    computational complexity :O(N)"""
    number_of_patient = 0
    for patient in data:
        if patient.age >= age_over:
            number_of_patient += 1
    return number_of_patient


def sick_patients(labname: str, gt_lt: str, value: float, data: list[Lab]) -> list[str]:
    """find sick patients in data confirmed by Three factors(lab, gt_lt, value)
    computational complexity :O(N*M)"""
    sick_patients = set()
    if gt_lt == ">":
        for lab in data:
            if lab.name == labname:
                if float(lab.value) > value:
                    sick_patients.add(lab.patientid)
    if gt_lt == "<":
        for lab in data:
            if lab.name == labname:
                if float(lab.value) > value:
                    sick_patients.add(lab.patientid)
    else:
        raise ValueError("gt_lt can only be choosen from > or <")
    return list(sick_patients)


def age_admission(
    patientid: str, data_lab: list[Lab], data_patient: list[Patient]
) -> float:
    """compare the birth year from patient*file with the earilst record year from lab*file
    The computational complexity of this function is O(N)"""
    date = datetime.now()

    find_data = FALSE
    for lab in data_lab:
        if lab.patientid == patientid:
            if lab.time < date:
                date = lab.time
                find_data = TRUE
                break
    if not find_data:
        raise ValueError("Patient is not in lab data.")

    find_data = FALSE
    for patient in data_patient:
        if patient.id == patientid:
            birthday = patient.dob
    if not find_data:
        raise ValueError("Patient is not in patient data.")
    age_at_admission = (date - birthday).days / 365.25
    return round(age_at_admission, 1)
