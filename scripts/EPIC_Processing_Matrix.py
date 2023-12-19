import numpy as np
import pandas as pd
import copy
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

"""
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("EPIC Processing Matrix").sheet1  # Open the spreadhseet
data = sheet.get_all_records()  # Get a list of all records
# row = sheet.row_values(3)  # Get a specific row
# col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell
print("--------------------------")
print(cell)
print("--------------------------")

insertRow = ["hello", 5, "red", "blue"]
sheet.add_rows(insertRow, 4)  # Insert the list as a row at index 4
sheet.update_cell(2,2, "CHANGED")  # Update one cell
numRows = sheet.row_count  # Get the number of rows in the sheet
"""
# py EPIC_Processing_Matrix.py

main_data = pd.read_excel("C:\\Users\\Arya\\Desktop\\EPIC Processing Matrix.xlsx", "Raw Data")
    
ms_IDs = []

# iterate through the Excel file and add subject ID with date to the dictionary
for row in main_data.iterrows():
    ms_IDs .append(row[1].MSID)




def lookup_mseids(ms_id, cache_file = None):
	"""
	"""
    if I_AM_DEBUGGING:
        print("looking for mse_ids associated with the folloing subject id (i.e. msID): {0}...".format(ms_id))

    if cache_file == None:
        output = sp.check_output(["ms_get_patient_imaging_exams", "--patient_id", "{0}".format(ms_id[2:])])
        parsed_output = str(output).split("\\n")
        only_data = parsed_output[5:]
        if len(only_data) == 1:
            if I_AM_DEBUGGING:
                print("...found no mseIds asscociated with the msId: {0}...".format(ms_id))
            return []
        else:
            mse_ids = []
            only_data = only_data[0: len(only_data) - 1 ]
            for line in only_data:
                mse_id, date = line.split()[0], line.split()[1]
                mse_ids.append(int(mse_id))
    else:
        if I_AM_DEBUGGING:
            print("...using cache files at path: {0}...".format(cache_file))
            print("...using key {0} which is of type {1}".format(ms_id[2:], type(ms_id[2:])))

        f = open(cache_file)
        lookup_table = json.load(f)['data']
        if ms_id[2:] in lookup_table:
            mse_ids = lookup_table[ms_id[2:]]

        else:
            print("...found no mseIds asscociated with the msId: {0}".format(ms_id))
            return []

    if I_AM_DEBUGGING:
        print("...found the following mseIds: {0}".format(mse_ids))

    return mse_ids