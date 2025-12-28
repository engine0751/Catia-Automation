import sys
from extractor.parameter_extractor import extract_parameters_to_csv

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_CATPart>")
        return

    part_path = sys.argv[1]
    extract_parameters_to_csv(part_path)
    print("Export complete.")

if __name__ == "__main__":
    main()