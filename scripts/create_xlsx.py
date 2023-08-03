from io import BytesIO
import pandas as pd


def create_xlsx(data):
    df = pd.DataFrame.from_records(data)
    with BytesIO() as excel_file:
        df.to_excel(excel_file, index=False)
        excel_file.seek(0)
        excel = excel_file.read()
    return excel
