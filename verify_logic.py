import pandas as pd
from datetime import datetime

# Create a sample excel
data = {
    'Date': ['1 Dec 2025', '2 Dec 2025'],
    'Amount': [100, 200],
    'Description': ['Test 1', 'Test 2'],
    'Category': ['Food', 'Travel']
}
df = pd.DataFrame(data)
df.to_excel('test_upload.xlsx', sheet_name='Dec', index=False)

print("Created test_upload.xlsx")

# Simulate parsing
try:
    xls = pd.ExcelFile('test_upload.xlsx')
    for sheet_name in xls.sheet_names:
        df = pd.read_excel('test_upload.xlsx', sheet_name=sheet_name)
        print(f"Sheet: {sheet_name}")
        for index, row in df.iterrows():
            date_val = row['Date']
            if isinstance(date_val, str):
                date_obj = datetime.strptime(date_val, '%d %b %Y').date()
            else:
                date_obj = date_val.date()
            
            print(f"Row {index}: {date_obj} - {row['Description']} - {row['Amount']} - {row['Category']}")
    print("Verification Successful")
except Exception as e:
    print(f"Verification Failed: {e}")
