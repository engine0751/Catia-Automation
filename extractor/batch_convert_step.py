import os
from pycatia import catia

def batch_convert_to_step(folder_path: str):
    catiapp = catia()
    for file in os.listdir(folder_path):
        if file.lower().endswith(".catpart"):
            inp=os.path.join(folder_path,file)
            out=os.path.join(folder_path,file.replace(".CATPART",".stp"))
            doc=catiapp.documents.open(inp)
            doc.export_data(out,"stp")
            doc.close()
