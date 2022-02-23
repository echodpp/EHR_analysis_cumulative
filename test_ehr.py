from ehr_analysis import parse_data
from ehr_analysis import age
from ehr_analysis import num_older_than
from ehr_analysis import sick_patients
from ehr_analysis import year
from ehr_analysis import age_admission


def test_parse_data():

    result = parse_data("PatientCorePopulatedTable.txt")
    expected = [
        [
            "PatientID",
            "PatientGender",
            "PatientDateOfBirth",
            "PatientRace",
            "PatientMaritalStatus",
            "PatientLanguage",
            "PatientPopulationPercentageBelowPoverty\n",
        ]
    ]
    assert result == expected


def test_age():

    result = age("1947-12-28 02:45:40.547")
    expected = 75
    assert result == expected


def test_num_older_than():

    result = num_older_than(
        60,
        [
            [
                "PatientID",
                "PatientGender",
                "PatientDateOfBirth",
                "PatientRace",
                "PatientMaritalStatus",
                "PatientLanguage",
                "PatientPopulationPercentageBelowPoverty",
            ]
        ],
    )
    expected = 0
    assert result == expected


def test_sick_patients():

    result = sick_patients(
        "URINALYSIS: RED BLOOD CELLS",
        ">",
        1,
        [
            [
                "\ufeffPatientID",
                "AdmissionID",
                "LabName",
                "LabValue",
                "LabUnits",
                "LabDateTime\n",
            ],
            [
                "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
                "1",
                "URINALYSIS: RED BLOOD CELLS",
                "1.8",
                "rbc/hpf",
                "1992-07-01 01:36:17.910\n",
            ],
        ],
    )
    expected = ["1A8791E3-A61C-455A-8DEE-763EB90C9B2C"]
    assert result == expected


def test_year():

    result = year("1947-12-28 02:45:40.547")
    expected = 1947
    assert result == expected


def test_age_admission():

    result = age_admission("1A8791E3-A61C-455A-8DEE-763EB90C9B2C")
    expected = 19
    assert result == expected
