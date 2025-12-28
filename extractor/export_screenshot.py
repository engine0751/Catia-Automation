from pycatia import catia

def export_screenshot(file_path: str, output_path: str = "screenshot.png"):
    catiapp = catia()
    docs = catiapp.documents
    part_doc = docs.open(file_path)

    viewer = part_doc.active_window.active_viewer
    viewer.reframe()
    viewer.fit_all()
    viewer.capture_to_file(output_path)

    part_doc.close()
