import argparse

parser = argparse.ArgumentParser(description="Positional vs Optional")

# Positional argument (required)
parser.add_argument("module", help="This is a positional module")

# Optional argument (uses flags)
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")

# Parse arguments
args = parser.parse_args()

print(f"Running module {args.module}")

if args.verbose:
    print("Verbose mode is ON")

else:
    print("Verbose is off")
    #commandline to run python -u "/home/SOLO/pithon/Phase 2/Argparse/positional_vs_optional.py" math -v