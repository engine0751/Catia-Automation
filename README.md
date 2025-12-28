🚀 CATIA Parameter & Automation Toolkit

A beginner-friendly Python automation toolkit for CATIA V5

This project provides a collection of simple, clean, and practical Python scripts that automate common CATIA V5 tasks using the pycatia library.
It is designed for beginners, students, and engineers who want to learn CATIA automation using Python and expand their workflow automation capabilities.

The toolkit includes:

✔ Parameter extraction

✔ Screenshot export

✔ Mass properties extraction

✔ Batch STEP conversion

✔ Geometry listing

✔ Point creation

✔ Clean project structure for learning & scaling

Whether you're new to CATIA automation or building your first Python–CATIA integration, this repository gives you a modular, ready-to-use starting point.

📂 Features Included
🔧 1. Parameter Extractor

Reads all parameters inside a CATPart and saves them to a CSV file.
Useful for documentation, analysis, or parametric model workflows.

📸 2. Screenshot Exporter

Automatically rotates the model and exports a clean PNG screenshot.
Great for previews, documentation, and automated reporting.

⚖️ 3. Mass Properties Exporter

Extracts body mass, volume, surface area, and center of gravity into a CSV.
Essential for engineering calculations and validations.

🔄 4. Batch STEP Converter

Converts all CATPart files in a folder into STEP (.stp) format.
Ideal for export workflows, supplier documentation, and CAD exchange.

🧱 5. Geometry Lister

Lists all bodies and sketches inside a CATPart.
Helps beginners understand the CATIA model tree programmatically.

🎯 6. Point Creator

Creates a 3D point at any XYZ coordinate inside a CATPart.
Small but powerful example of geometry creation through automation.

📦 Project Structure
CATIA-Parameter-Extractor/
│
├── README.md
├── main.py
├── extractor/
│   ├── parameter_extractor.py
│   ├── export_screenshot.py
│   ├── mass_properties.py
│   ├── batch_convert_step.py
│   ├── list_geometry.py
│   ├── create_point.py
│   └── __init__.py
└── sample/
    └── sample_usage.txt

🚀 Getting Started
1. Install Python Dependencies
pip install pycatia

2. Run Any Tool

Example: Extract parameters from a CATPart

python main.py "C:/path/to/your/part.CATPart"

🎯 Who This Project Is For

CATIA beginners

Students learning CAD automation

Engineers who want to automate repetitive CATIA tasks

Developers exploring Python–CATIA integration

Anyone creating an automation portfolio project for GitHub

📝 License

You can choose the license you prefer (MIT recommended).
If you want, I can generate it for you automatically.

📥 Download

Full project ZIP file is included for convenience:

CATIA-Parameter-Extractor.zip