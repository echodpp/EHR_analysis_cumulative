# %% [markdown]
# # Computational complexity/Data structures


# %% [markdown]
# ## Data parsing

# %%
def parse_data(path_to_file: str) -> list[list[str]]:
    "read file.txt to a list line by line and split by tab\t"
    "computational complexity :0(N)"
    with open(path_to_file) as file:
        lines = file.readlines()
    data = []
    for i in lines:  # N times
        data.append(i.split("\t"))  # O(1)
    return data


# %% [markdown]
# ## Analysis


# %% [markdown]
# ### Old patients

# %%
def age(a: str) -> int:
    """change format of date and transfer into ages(compare with 2022)"""
    return 2022 - int(a.split()[0].split("-")[0])


# %%
def num_older_than(age_over: int, data: list[list[str]]) -> int:
    """compare ages line by line in data with chosen number(age_over),and return the total number of patients"
    computational complexity :0(N)"""
    number_of_patient = 0
    for i, line in enumerate(data):  # N times
        if i > 0:  # O(1)
            if age(line[2]) >= age_over:  # O(1)
                number_of_patient += 1  # O(1)
    return number_of_patient


# %% [markdown]
# ### Sick patients

# %%
def sick_patients(
    lab: str, gt_lt: str, value: float, data: list[list[str]]
) -> list[str]:
    """find sick patients in data confirmed by Three factors(lab, gt_lt, value)
    computational complexity :0(N)"""
    df = []
    if gt_lt == ">":  # O(1)
        for i, line in enumerate(data):  # N times
            if i > 0:  # O(1)
                if line[2] == lab:  # O(1)
                    if float(line[-3]) > value:  # O(1)
                        df.append(line[0])  # O(1)
    if gt_lt == "<":  # O(1)
        for i, line in enumerate(data):  # N times
            if i > 0:  # O(1)
                if line[2] == lab:  # O(1)
                    if float(line[-3]) < value:  # O(1)
                        df.append(line[0])  # O(1)
    else:
        raise ValueError("gt_lt can only be choosen from > or <")
    return df


# %% [markdown]
# ### Age of patients when admission


def year(Date: str) -> int:
    """change format of date only keep year"""
    return int(Date.split()[0].split("-")[0])


def age_admission(patientid: str) -> int:
    """compare the birth year from patient*file with the earilst record year from lab*file"""
    df1 = parse_data("LabsCorePopulatedTable.txt")
    df2 = parse_data("PatientCorePopulatedTable.txt")
    test_date = []
    for i, line in enumerate(df1):
        if i > 0:
            if line[0] == "patientid":
                test_date.append(year(line[-1]))
            else:
                raise ValueError("patientid can not be found in df1")
    for i, line in enumerate(df2):
        if i > 0:
            if line[0] == "1A8791E3-A61C-455A-8DEE-763EB90C9B2C":
                birthyear = year(line[2])
            else:
                raise ValueError("patientid can not be found in df2")
    test_date.sort()
    age_at = test_date[0] - birthyear
    return age_at
