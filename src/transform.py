import zipfile
import pandas as pd
from pathlib import Path

def process_data(path: Path, zip_file_path: Path):
    """Unzipping file"""
    loan_csv_filename = None

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        all_files = zip_ref.namelist()

        for file in all_files:
            if file.endswith(".csv"):
                loan_csv_filename = file
                break

        if not loan_csv_filename:
            raise FileNotFoundError(f"Could not find loan csv file in {zip_file_path}")

        """Extraction"""
        print("Extracting {}".format(zip_file_path))
        zip_ref.extractall(path)
        print("Extracting finished")

    """Dataframe loading and basic transformations"""
    required_columns = ['loan_amnt', 'term', 'int_rate', 'grade', 'emp_length', 'home_ownership', 'annual_inc',
                        'verification_status', 'issue_d', 'loan_status', 'purpose', 'dti', 'earliest_cr_line',
                        'addr_state']


    loan_file_path = path / loan_csv_filename
    df = pd.read_csv(loan_file_path, usecols=required_columns, skiprows=1, skipfooter=2)
    df["emp_length"] = df["emp_length"].fillna("Unknown")
    df["int_rate"] = df["int_rate"].str.strip().str.rstrip("%").astype("float")
    df["issue_d"] = pd.to_datetime(df["issue_d"], format="%b-%Y")
    print(df.info())
    print(df.head(5))
    return df
