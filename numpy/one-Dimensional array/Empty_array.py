import numpy as np

# Define a list of records
records = [(1, 'Alice', 25.5), (2, 'Bob', 30.0), (3, 'Charlie', 28.0)]

# Define the data type
dtype = [('id', 'i4'), ('name', 'U10'), ('age', 'f4')]

# Create the structured array
structured_array = np.rec.fromrecords(records, dtype=dtype)

print(structured_array)