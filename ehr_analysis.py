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

    def __init__(self, ID, Labname, Value, Units, Labtime):
        self.ID = ID
        self.Value = Value
        self.Labname = Labname
        self.Units = Units
        self, Labtime = Labtime


def parse_data_patient(path_to_file: str) -> dict[str, Patient]:
    "read patient.txt to a list line by line and split by tab\t"
    "computational complexity :0(N)"
    with open(path_to_file) as file:
        lines = file.readlines()
    data = dict()
    for i, line in enumerate(lines):
        if i > 0:
            ID, GENDER, DOB, RACE, _, _, _ = line.split("\t")
            data[ID] = Patient(ID, GENDER, DOB, RACE)
    return data


print(parse_data_patient("PatientCorePopulatedTable.txt"))


def parse_data_lab(path_to_file: str) -> dict[str, Lab]:
    "read labs.txt to a list line by line and split by tab\t"
    "computational complexity :0(N)"
    with open(path_to_file) as file:
        lines = file.readlines()
    data = dict()
    for i, line in enumerate(lines):
        if i > 0:
            ID, _, Labname, Value, Units, Labtime = line.split("\t")
            data[ID] = Lab(ID, Labname, Value, Units, Labtime)
    return data


def num_older_than(age_over: int, data: dict[str, Patient]) -> int:
    """Calculate number of patients older than a given age"
    computational complexity :0(N)"""
    number_of_patient = 0
    for patient in data.values():
        if patient.age() >= age_over:
            number_of_patient += 1
    return number_of_patient


def sick_patients(
    lab: str, gt_lt: str, value: float, data: dict[str, Lab]
) -> list[str]:
    """find sick patients in data confirmed by Three factors(lab, gt_lt, value)
    computational complexity :0(N)"""
    sick_patients = set()
    if gt_lt == ">":
        for patient in data.values():
            if patient.Labname == lab:
                if patient.Value > value:
                    sick_patients.add(patient.ID)
    if gt_lt == "<":
        for patient in data.values():
            if patient.Labname == lab:
                if patient.Value > value:
                    sick_patients.add(patient.ID)
    else:
        raise ValueError("gt_lt can only be choosen from > or <")
    return sick_patients


def age_admission(
    patientid: str, data1: dict[str, Lab], data2: dict[str, Patient]
) -> int:
    """compare the birth year from patient*file with the earilst record year from lab*file"""
    data = 2022
    if patientid in data1:
        for patient in data1:
            if data1.Labtime < data:
                date = data1.Labtime
    else:
        raise PatientError("Patient is not in lab data.")
    if patientid in data2:
        for patient in data2:
            birthyear = int(patient.DOB.split()[0].split("-")[0])
    else:
        raise PatientError("Patient is not in patient data.")
    age_at_admission = date - birthyear
    return age_at_admission
