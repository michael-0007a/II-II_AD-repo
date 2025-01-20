import pandas as pd

patient_data = {
    'Patient Name': ['Michael', 'Rithik', 'Harsha', 'Deepak'],
    'Age': [5, 32, 6, 4],
    'Date of Appointment': ['2025-01-10', '2025-01-12', '2025-01-15', '2025-01-20'],
    'Patient ID': [1, 2, 3, 4]
}
patient_df = pd.DataFrame(patient_data)

drug_quantity_data = {
    'Drug Name': ['Paracetamol', 'Ibuprofen', 'Amoxicillin', 'Cough Syrup'],
    'Quantity': [2, 1, 3, 1],
    'Patient ID': [1, 2, 3, 4]
}
drug_quantity_df = pd.DataFrame(drug_quantity_data)

# patients with Age < 6
filtered_patients = patient_df.loc[patient_df['Age'] < 6, ['Patient Name', 'Age']]

# Merge the DataFrames with an inner join on 'Patient ID'
merged_df = pd.merge(patient_df, drug_quantity_df, on='Patient ID', how='inner')

# Display outputs
print("Patient DataFrame:")
print(patient_df)

print("\nDrug Quantity DataFrame:")
print(drug_quantity_df)

print("\nFiltered Patients (Age < 6):")
print(filtered_patients)

print("\nMerged DataFrame:")
print(merged_df)
