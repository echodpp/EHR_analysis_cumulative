import sqlite3

con = sqlite3.connect("mydatabase.db")
c = con.cursor()

# read the data in list of list
def parse_data(path_to_file: str) -> list[list[str]]:
    "read file.txt to a list line by line and split by tab\t"
    "computational complexity :0(N)"
    with open(path_to_file) as file:
        lines = file.readlines()
    data = []
    for i, line in enumerate(lines):
        if i > 0:  # N times
            data.append(line.strip("\n").split("\t"))  # O(1)
    return data


patients = parse_data("PatientCorePopulatedTable.txt")
labs = parse_data("LabsCorePopulatedTable.txt")

# insert patient table
c.execute(
    """CREATE TABLE IF NOT EXISTS patient (id TEXT PRIMARY KEY,gender TEXT,dob INTEGER,race TEXT,marital TEXT,language TEXT,pbp REAL)"""
)
c.executemany("INSERT INTO patient VALUES (?,?,?,?,?,?,?)", patients)


# insert lab table
c.execute(
    """CREATE TABLE IF NOT EXISTS lab (patientid TEXT,admissionid TEXT,name TEXT,value TEXT,unit TEXT,dot INTEGER)"""
)
c.executemany("INSERT INTO lab VALUES (?,?,?,?,?,?)", labs)

# join the seclected columns to final tabel
c.execute(
    """CREATE TABLE IF NOT EXISTS final (patientid TEXT,dob TEXT,labname TEXT,value TEXT,dot INTEGER)"""
)
c.execute(
    """INSERT INTO final
Select p.id, p.dob, l.name,l.value,l.dot From patient p JOIN lab l on p.id = l.id"""
)

# check the results
for row in c.execute("SELECT * FROM new_records"):
    print(row)
