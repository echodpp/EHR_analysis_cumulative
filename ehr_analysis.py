class Patient(object):
    """Patient information'"""

    def __init__(self, ID, GENDER, DOB, RACE):
        self.ID = ID
        self.DOB = DOB
        self.GENDER = GENDER
        self.RACE = RACE

    def age(self) -> float:
        return 2022 - int(self.DOB.split()[0].split("-")[0])


class Lab(object):
    """Patient's lab information"""

    def __init__(self, id, Labname, Value, Units, Labtime):
        self.ID = id
        self.Labname = Labname
        self.Value = Value
        self.Units = Units
        self.Labtime = Labtime


def parse_data_patient(path_to_file: str) -> list[Patient]:
    "read patient.txt to a list line by line and split by tab\t"
    "computational complexity :0(N)"
    with open(path_to_file) as file:
        lines = file.readlines()
    data = []
    for i, line in enumerate(lines):
        if i > 0:
            ID, GENDER, DOB, RACE, _, _, _ = line.split("\t")
            data.append(Patient(ID, GENDER, DOB, RACE))
    return data


<<<<<<< HEAD
def parse_data_lab(path_to_file: str) -> list[Lab]:
=======
def parse_data_lab(path_to_file: str) -> dict[str, Lab]:
>>>>>>> d6692a97d246e626cf27aa1abe13e44a8b2196fd
    "read labs.txt to a list line by line and split by tab\t"
    "computational complexity :0(N)"
    with open(path_to_file) as file:
        lines = file.readlines()
    data = []
    for i, line in enumerate(lines):
        if i > 0:
            id, _, Labname, Value, Units, Labtime = line.split("\t")
            data.append(Lab(id, Labname, Value, Units, Labtime))
    return data


def num_older_than(age_over: int, data: list[Patient]) -> int:
    """Calculate number of patients older than a given age"
    computational complexity :0(N)"""
    number_of_patient = 0
    for patient in data:
        if patient.age() >= age_over:
            number_of_patient += 1
    return number_of_patient


def sick_patients(lab: str, gt_lt: str, value: float, data: list[Lab]) -> list[str]:
    """find sick patients in data confirmed by Three factors(lab, gt_lt, value)
    computational complexity :0(N)"""
    sick_patients = set()
    if gt_lt == ">":
        for patient in data:
            if patient.Labname == lab:
                if float(patient.Value) > value:
                    sick_patients.add(patient.ID)
    if gt_lt == "<":
        for patient in data:
            if patient.Labname == lab:
                if float(patient.Value) > value:
                    sick_patients.add(patient.ID)
    else:
        raise ValueError("gt_lt can only be choosen from > or <")
    return sick_patients


def age_admission(
    patientid: str, data_lab: list[Lab], data_patient: list[Patient]
) -> int:
    """compare the birth year from patient*file with the earilst record year from lab*file"""
    date = 2022
    for patient in data_lab:
        if patient.ID == patientid:
            if int(patient.Labtime.split()[0].split("-")[0]) < date:
                date = int(patient.Labtime.split()[0].split("-")[0])

    for patient in data_patient:
        if patient.ID == patientid:
            birthyear = int(patient.DOB.split()[0].split("-")[0])

    age_at_admission = date - birthyear
    return age_at_admission
