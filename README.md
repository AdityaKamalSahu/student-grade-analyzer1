# Student Performance Intelligence

A learning-focused ML project built step by step while learning Python, NumPy, Pandas, and Machine Learning.

## V1 — NumPy Data Generation Pipeline

Current version generates a synthetic dataset for 100 students using NumPy.

### Current pipeline

1. Generate random student data
2. Convert study hours and assignment counts into score scales
3. Calculate a weighted performance score
4. Combine features into a 2D NumPy dataset
5. Inspect the dataset shape and sample rows
6. Save the dataset as `data/students.csv`

### Features

- `study_hours`
- `attendance`
- `assignments_score`
- `previous_score`
- `performance_score`

## Run

From the project root:

```bash
python src/data_generator.py
```

## Project Status

**V1 complete:** NumPy-based synthetic data generation.

Next: dataset analysis with Pandas/NumPy.
