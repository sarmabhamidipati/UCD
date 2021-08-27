"""
Extract a function
Writing a function to calculate the z-scores would improve this code.

# Standardize the GPAs for each year
df['y1_z'] = (df.y1_gpa - df.y1_gpa.mean()) / df.y1_gpa.std()
df['y2_z'] = (df.y2_gpa - df.y2_gpa.mean()) / df.y2_gpa.std()
df['y3_z'] = (df.y3_gpa - df.y3_gpa.mean()) / df.y3_gpa.std()
df['y4_z'] = (df.y4_gpa - df.y4_gpa.mean()) / df.y4_gpa.std()

Note: df is a pandas DataFrame where each row is a student with 4 columns of yearly student
      GPAs: y1_gpa, y2_gpa, y3_gpa, y4_gpa

    Finish the function so that it returns the z-scores of a column.
    Use the function to calculate the z-scores for each year (df['y1_z'], df['y2_z'], etc.)
    from the raw GPA scores (df.y1_gpa, df.y2_gpa, etc.).

"""
import pandas as pd

df = pd.read_csv("student_gpa.csv")
print(df.head())


def standardize(column):
    """Standardize the values in a column.

  Args:
    column (pandas Series): The data to standardize.

  Returns:
    pandas Series: the values as z-scores
  """
    # Finish the function so that it returns the z-scores
    z_score = (column - column.mean()) / column.std()
    return z_score


# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df.y1_gpa)
df['y2_z'] = standardize(df.y2_gpa)
df['y3_z'] = standardize(df.y3_gpa)
df['y4_z'] = standardize(df.y4_gpa)

print(df.head())
