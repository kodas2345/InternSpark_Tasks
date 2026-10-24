
import pandas as pd

# Load CSV file
df = pd.read_csv("student.csv")

print("Original Data:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Filter students scoring above 80
print("\nStudents scoring above 80:")
print(df[df["Marks"] > 80])

# Group students by city
print("\nAverage Marks by City:")
print(df.groupby("City")["Marks"].mean())

print("\nData analysis completed!")
