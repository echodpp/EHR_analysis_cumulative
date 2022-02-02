# %% [markdown]
# # Computational complexity/Data structures

# %% [markdown]
# ## Data parsing

# %%
def parse_data(path_to_file: str)->list:
    "read file.txt to a list line by line and split by tab\t"
    "computational complexity :0(N)"
    with open(path_to_file)as file:
        lines=file.readlines()
    data=[]
    for i in lines:# N times
        data.append(i.split('\t'))# O(1)
    return data

# %% [markdown]
# ## Analysis

# %% [markdown]
# ### Old patients

# %%
import datetime

# %%
def age(a):
    "change format of date and transfer into ages(compare with 2022)"
    return 2022-datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S').year


# %%
def num_older_than(age_over, data):
    "compare ages line by line in data with chosen number(age_over),and return the total number of patients"
    "computational complexity :0(N)"
    number_of_patient=0
    for i,line in enumerate(data):# N times
        if i>0:# O(1)
            if int(age(line[-1]))>=age_over:# O(1)
                number_of_patient+=1# O(1)
    
    return number_of_patient

# %% [markdown]
# ### Sick patients

# %%
def sick_patients(lab, gt_lt, value, data):
    "find sick patients in data confirmed by Three factors(lab, gt_lt, value)"
    "computational complexity :0(N)"
    df=[]
    if gt_lt=='>':# O(1)
     for i,line in enumerate(data):# N times
        if i>0:# O(1)
            if line[2]==lab:# O(1)
                if float(line[-3])> value:# O(1)
                    df.append(line[0])# O(1)
    if gt_lt=='<':# O(1)
     for i,line in enumerate(data):# N times
        if i>0:# O(1)
            if line[2]==lab:# O(1)
                if float(line[-3])< value:# O(1)
                    df.append(line[0]) # O(1)


