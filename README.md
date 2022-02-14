# Getting Started
several python module here to provides some simple analytical capabilities on some (synthetic) EHR data
the expected input file formats is txt file ：
A table of patients with demographic data: PatientCorePopulatedTable.txt
A table of laboratory results: LabsCorePopulatedTable.txt
* For a full description of the module:
parse_data:`parse_data(filename: str) -> list[list[str]]`  reads and parses the data files for further analysis.
age:`age(a: str) -> int` is read year out for ages calculation from  format of '1992-07-01 01:36:17.910\n'
num_older_than:` num_older_than(age_over: int, data: list[list[str]]) -> int` count how many patients from (data) are over certain ages(age_over)
sick_patients：` sick_patients(lab: str, gt_lt: str, value: float, data: list[list[str]]) -> list[str]` return a list of patients ID from (data) of certain (lab) , with 'LabValue'  greater or less than a certain (value)
# Requirements
no packges required
# Installation
nstall the module from ehr_analysis.py at https://github.com/xiaoyudpp/-_private_-
# API description
 don't know how to write this 
# Running the tests
there are test file included for testing with the `pytest` framework
example: 
def test_age():
    from ehr_analysis import age

    result = age("1947-12-28 02:45:40.547")
    expected = 75
    assert result == expected

