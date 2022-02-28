import ehr_analysis as ehr


def test_parse_data():

    result = ehr.parse_data("LabsCorePopulatedTable.txt")
    assert len(result) == 111483


def test_num_older_than():

    result = ehr.num_older_than(60, ehr.parse_data("PatientCorePopulatedTable.txt"))
    expected = 58
    assert result == expected


def test_sick_patients():

    result = ehr.sick_patients(
        "URINALYSIS: RED BLOOD CELLS",
        ">",
        1,
        ehr.parse_data("LabsCorePopulatedTable.txt"),
    )
    expected = 1
    assert len(result) == expected


def test_age_admission():

    result = ehr.age_admission(
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
        ehr.parse_data("LabsCorePopulatedTable.txt"),
        ehr.parse_data("PatientCorePopulatedTable.txt"),
    )
    expected = 18.9
    assert result == expected
