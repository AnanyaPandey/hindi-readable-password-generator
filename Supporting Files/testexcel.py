import openpyxl
import os 

# Load the Excel workbook
os.chdir(r"G:\py\passowordgen")
file_path = 'PasswordRecords.xlsx'  # Replace with the path to your Excel file

workbook = openpyxl.load_workbook(file_path)

# Select the active worksheet
worksheet = workbook.active

# Check if the first row is empty
first_row_empty = all(cell.value is None for cell in worksheet[1])


if first_row_empty:
    print("The first row is empty.")
    header = ["First Name","Last Name","Age"]
    worksheet.append(header)
else:
    print("The first row is not empty.")
    R1 = ["Ananya","Pandey",34]
    worksheet.append()

workbook.save("PasswordRecords.xlsx")
# Close the workbook
workbook.close()
