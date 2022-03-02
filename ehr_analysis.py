from datetime import datetime


class Patient(object):
    """Patient information'"""

    def __init__(self, id: str, gender: str, dob: str, race: str):
        """declare variables in the class patient"""
        self.id = id
        self.dob = datetime.fromisoformat(dob)
        self.gender = gender
        self.race = race

    @property
    def age(self) -> float:
        """return patient's age"""
        today = datetime.now()
        current_age = today - self.dob
        return current_age.days / 365.25


class Lab(object):
    """Patient's lab information"""

    def __init__(self, patientid: str, name: str, value: str, units: str, time: str):
        """declare variables in the class lab"""
        self.patientid = patientid
        self.name = name
        self.value = value
        self.units = units
        self.time = datetime.fromisoformat(time)


def parse_data(path_to_file: str) -> list[Lab] or list[Patient]:
    "read labs.txt to a list line by line and split by tab\t"
    "computational complexity :O(N*M)"
    with open(path_to_file) as file:
        lines = file.readlines()
    data = []
    for i, line in enumerate(lines):
        if i > 0:
            if path_to_file == "LabsCorePopulatedTable.txt":
                patientid, _, name, value, units, time = line.strip("\n").split("\t")
                data.append(Lab(patientid, name, value, units, time))
            if path_to_file == "PatientCorePopulatedTable.txt":
                id, gender, dob, race, _, _, _ = line.strip("\n").split("\t")
                data.append(Patient(id, gender, dob, race))
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
    for lab in data_lab:
        if lab.patientid == patientid:
            if lab.time < date:
                date = lab.time
        else:
            raise ValueError("Patient is not in lab data.")

    for patient in data_patient:
        if patient.id == patientid:
            birthday = patient.dob
        else:
            raise ValueError("Patient is not in patient data.")
    age_at_admission = (date - birthday).days / 365.25
    return round(age_at_admission, 1)
