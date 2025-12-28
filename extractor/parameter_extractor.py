import csv
from pycatia import catia

def extract_parameters_to_csv(file_path: str):
    catiapp = catia()
    docs = catiapp.documents
    part_doc = docs.open(file_path)
    part = part_doc.part

    parameters = part.parameters
    rows = []
    for i in range(parameters.count):
        param = parameters.item(i + 1)
        try:
            rows.append([param.name, param.value_as_string, param.type])
        except:
            continue

    with open("exported_parameters.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows([["Name","Value","Type"], *rows])

    part_doc.close()