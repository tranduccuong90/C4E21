import pyexcel

#1. Prepare data

data = [
    {
        'name': "Cuong",
        'age': 28,
    },
    {
        'name': "Quan",
        'age': 19,
    },
    {
        'name': "Duc",
        'age': 18,
    },
]

#2. Save
pyexcel.save_as(records=data, dest_file_name = "sample.xlsx")