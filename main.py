from pathlib import Path

from src.extract import download_file
from src.load import load_to_postgres
from src.transform import process_data

PROJECT_ROOT = Path(__file__).parent

def main():
    data_folder_path = PROJECT_ROOT / "data" / "raw"
    loan_data_url = "https://resources.lendingclub.com/LoanStats_2018Q4.csv.zip"

    data_folder_path.mkdir(parents=True, exist_ok=True)

    downloaded_zip_path = download_file(loan_data_url, data_folder_path)

    loan_df = process_data(data_folder_path, zip_file_path=downloaded_zip_path)

    load_to_postgres(df=loan_df, table_name='loan')

if __name__ == "__main__":
    main()