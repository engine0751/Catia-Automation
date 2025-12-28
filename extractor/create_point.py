from pycatia import catia

def create_point(file_path: str, x=0, y=0, z=0):
    catiapp = catia()
    doc = catiapp.documents.open(file_path)
    part = doc.part
    factory = part.hybrid_shape_factory

    point = factory.add_new_point_coord(x,y,z)
    part.hybrid_bodies.item(1).append_hybrid_shape(point)

    part.update()
    doc.save()
    doc.close()
