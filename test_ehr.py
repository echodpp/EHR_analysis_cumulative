import ehr_analysis as ehr


def test_parse_data():

    result = ehr.parse_data("PatientCorePopulatedTable.txt")
    assert len(result) == 10


def test_num_older_than():

    result = ehr.num_older_than(60, ehr.parse_data("PatientCorePopulatedTable.txt"))
    expected = 6
    assert result == expected


def test_sick_patients():
    data = ehr.parse_data("LabsCorePopulatedTable.txt")
    result = ehr.sick_patients(
        "URINALYSIS: RED BLOOD CELLS",
        "<",
        1,
        data,
    )
    expected = ["1A8791E3-A61C-455A-8DEE-763EB90C9B2C"]
    assert len(result) == expected


def test_age_admission():
    data_patient = ehr.parse_data("PatientCorePopulatedTable.txt")
    data_lab = ehr.parse_data("LabsCorePopulatedTable.txt")
    result = ehr.age_admission(
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
        data_patient,
        data_lab,
    )
    expected = 18.9
    assert result == expected
