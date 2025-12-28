import csv
from pycatia import catia

def export_mass_properties(file_path: str, csv_output="mass_properties.csv"):
    catiapp = catia()
    docs = catiapp.documents
    part_doc = docs.open(file_path)
    part = part_doc.part
    inertia = part.inertia

    props = {
        "Mass": inertia.mass,
        "Volume": inertia.volume,
        "Surface Area": inertia.surface_area,
        "CG X": inertia.center_of_gravity.x,
        "CG Y": inertia.center_of_gravity.y,
        "CG Z": inertia.center_of_gravity.z,
    }

    with open(csv_output,"w",newline="") as f:
        w=csv.writer(f); w.writerow(["Property","Value"])
        for k,v in props.items(): w.writerow([k,v])

    part_doc.close()