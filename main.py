from pathlib import Path

from src.extract import download_file


def main():
    home_dir = Path('src').home()
    data_folder_path = home_dir / "Desktop" / "projects" / "etl-loan-banking" / "data" / "raw"
    loan_data_url = "https://resources.lendingclub.com/LoanStats_2018Q4.csv.zip"

    download_file(loan_data_url, data_folder_path)

if __name__ == "__main__":
    main()