import ehr_analysis as ehr
import os


def test_parse_data():
    os.remove("new_db.db")
    result = ehr.parse_data("PatientCorePopulatedTable.txt")
    assert len(result) == 10


def test_num_older_than():
    os.remove("new_db.db")
    result = ehr.num_older_than(60, ehr.parse_data("PatientCorePopulatedTable.txt"))
    expected = 6
    assert result == expected


def test_sick_patients():
    os.remove("new_db.db")
    data = ehr.parse_data("LabsCorePopulatedTable.txt")
    result = ehr.sick_patients(
        "URINALYSIS: RED BLOOD CELLS",
        "<",
        1,
        data,
    )
    assert len(result) == 1


def test_age_admission():
    os.remove("new_db.db")
    data_patient = ehr.parse_data("PatientCorePopulatedTable.txt")
    data_lab = ehr.parse_data("LabsCorePopulatedTable.txt")

    result = ehr.age_admission(
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C", data_lab, data_patient
    )
    expected = 18.9
    assert result == expected
