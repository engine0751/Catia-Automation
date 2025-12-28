from pycatia import catia

def list_geometrical_elements(file_path: str):
    catiapp = catia()
    doc = catiapp.documents.open(file_path)
    part = doc.part

    for i in range(part.bodies.count):
        body = part.bodies.item(i+1)
        print("Body:", body.name)
        for j in range(body.sketches.count):
            print("  Sketch:", body.sketches.item(j+1).name)

    doc.close()