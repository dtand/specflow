import os
import shutil
import argparse
from antlr4 import FileStream, CommonTokenStream
from spec_grammar.SpecFileLexer import SpecFileLexer
from spec_grammar.SpecFileParser import SpecFileParser

# Parse the FEATURES section from an epic spec file
def parse_features(epic_path):
    features = []
    with open(epic_path, 'r') as f:
        lines = f.readlines()
    in_features = False
    for line in lines:
        if line.strip().startswith('FEATURES:'):
            in_features = True
            continue
        if in_features:
            if line.strip().startswith('-'):
                feature = line.strip()[1:].strip()
                if feature:
                    features.append(feature)
            elif line.strip() == '' or not line.startswith(' '):
                break
    return features

# spec init command

def validate_epic_spec(epic_path):
    try:
        input_stream = FileStream(epic_path)
        lexer = SpecFileLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = SpecFileParser(stream)
        tree = parser.specfile()
        # If parsing succeeds, return True
        return True
    except Exception as e:
        print(f"Validation error: {e}")
        return False

def spec_init(epic_path=None):
    # If no path provided, use epic.spec in current directory
    if epic_path is None:
        epic_path = os.path.join(os.getcwd(), 'epic.spec')
        if not os.path.isfile(epic_path):
            print("Error: No epic.spec file found in current directory.")
            return
    # Validate epic spec file
    if not validate_epic_spec(epic_path):
        print("Error: Epic spec file failed validation against grammar.")
        return
    epic_filename = os.path.basename(epic_path)
    epic_name, _ = os.path.splitext(epic_filename)
    requirements_dir = os.path.join(os.getcwd(), 'requirements')
    epic_dir = os.path.join(requirements_dir, epic_name)
    os.makedirs(epic_dir, exist_ok=True)
    # Copy epic file into epic_dir
    shutil.copy2(epic_path, os.path.join(epic_dir, epic_filename))
    # Parse features
    features = parse_features(epic_path)
    for feature in features:
        feature_dir = os.path.join(epic_dir, feature)
        os.makedirs(feature_dir, exist_ok=True)
        # Create empty <feature_name>.spec file
        spec_file_path = os.path.join(feature_dir, f"{feature}.spec")
        with open(spec_file_path, 'w') as sf:
            sf.write("")
    print(f"Initialized epic '{epic_name}' with features: {', '.join(features)}")

# CLI setup

def main():
    parser = argparse.ArgumentParser(description='Spec CLI toolkit')
    subparsers = parser.add_subparsers(dest='command')

    # spec init
    init_parser = subparsers.add_parser('init', help='Initialize project from epic spec file')
    init_parser.add_argument('epic_path', nargs='?', default=None, help='Path to epic spec file (optional)')

    args = parser.parse_args()
    if args.command == 'init':
        spec_init(args.epic_path)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
