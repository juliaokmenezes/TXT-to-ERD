
import json
import subprocess
from generation import call


def run_erdot(input_file, output_file):
    cmd = ["python", "-m", "ERDot.erdot.__main__", input_file, "-o", output_file]
    print(cmd)
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print(result)
    
    if result.returncode != 0:
        print(f"Error running ERDot: {result.stderr}")
        return None
    
    print(f"ERDot output saved to {output_file}")
    return output_file

