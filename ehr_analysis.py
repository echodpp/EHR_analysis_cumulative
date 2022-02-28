from datetime import datetime
class Patient(object):
    """Patient information'"""

    def __init__(self, ID, GENDER, DOB, RACE):
        self.ID = ID
        self.DOB = datetime.fromisoformat(DOB)
        self.GENDER = GENDER
        self.RACE = RACE
    @property
    def age(self) -> float:
        today = datetime.now()
        current_age = today - self.DOB
        return current_age.days / 365.25


class Lab(object):
    """Patient's lab information"""

    def __init__(self, id, Labname, Value, Units, Labtime):
        self.ID = id
        self.Labname = Labname
        self.Value = Value
        self.Units = Units
        self.Labtime = datetime.fromisoformat(Labtime)


def parse_data(path_to_file: str) -> list[Lab] or list[Patient] :
    "read labs.txt to a list line by line and split by tab\t"
    "computational complexity :O(N*M)"
    with open(path_to_file) as file:
        lines = file.readlines()
    data = []
    for i, line in enumerate(lines):
        if i > 0:
            if path_to_file=='LabsCorePopulatedTable.txt':
                id, _, Labname, Value, Units, Labtime = line.strip("\n").split("\t")
                data.append(Lab(id, Labname, Value, Units, Labtime))
            if path_to_file=='PatientCorePopulatedTable.txt':
                ID, GENDER, DOB, RACE, _, _, _ = line.strip('\n').split("\t")
                data.append(Patient(ID, GENDER, DOB, RACE))
    return data


def num_older_than(age_over: int, data: list[Patient]) -> int:
    """Calculate number of patients older than a given age"
    computational complexity :O(N)"""
    number_of_patient = 0
    for patient in data:
        if patient.age >= age_over:
            number_of_patient += 1
    return number_of_patient


def sick_patients(lab: str, gt_lt: str, value: float, data: list[Lab]) -> list[str]:
    """find sick patients in data confirmed by Three factors(lab, gt_lt, value)
    computational complexity :O(N*M)"""
    sick_patients = set()
    if gt_lt == ">":
        for lab in data:
            if lab.Labname == lab:
                if float(lab.Value) > value:
                    sick_patients.add(lab.ID)
    if gt_lt == "<":
        for lab in data:
            if lab.Labname == lab:
                if float(lab.Value) > value:
                    sick_patients.add(lab.ID)
    else:
        raise ValueError("gt_lt can only be choosen from > or <")
    return list(sick_patients)


def age_admission(
    patientid: str, data_lab: list[Lab], data_patient: list[Patient]
) -> int:
    """compare the birth year from patient*file with the earilst record year from lab*file
    The computational complexity of this function is O(N)"""
    date = datetime.now()
    for lab in data_lab:
        if lab.ID == patientid:
            if lab.Labtime < date:
                date = lab.Labtime
        else:
            raise ValueError("Patient is not in data.")

    for patient in data_patient:
        if patient.ID == patientid:
            birthday = patient.DOB
        else:
            raise ValueError("Patient is not in data.")
    age_at_admission = (date - birthday).days/365.25
    return age_at_admission
    