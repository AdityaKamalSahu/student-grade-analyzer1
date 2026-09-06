import numpy as np

np.random.seed(42)

study_hours = np.random.uniform(1, 10, 100)
study_score = study_hours / 10 * 100

attendance = np.random.uniform(40, 100, 100)

assignments = np.random.randint(0, 11, 100)
assignments_score = assignments / 10 * 100

previous_score = np.random.uniform(30, 100, 100)

performance_score = (
    study_score * 0.30 +
    attendance * 0.25 +
    assignments_score * 0.20 +
    previous_score * 0.25
)

data = np.column_stack((
    study_hours,
    attendance,
    assignments_score,
    previous_score,
    performance_score
))

columns = [
    "study_hours",
    "attendance",
    "assignments_score",
    "previous_score",
    "performance_score"
]

print(data.shape)
print(data[:5])
print(columns)

np.savetxt(
    "data/students.csv",
    data,
    delimiter=",",
    header="study_hours,attendance,assignments_score,previous_score,performance_score",
    comments=""
)
