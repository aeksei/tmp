# C:/Users/aeksei/AppData/Local/Programs/Python/Python39/python.exe -m pip install pandas
# C:/Users/aeksei/AppData/Local/Programs/Python/Python39/python.exe -m pip install openpyxl

import pandas as pd


def main():
    """
    Генерируем отчет с новыми вычисляемыми столбцами
    """
    excel_file = "products.xlsx"

    df = get_coasts_df(excel_file)
    print(df.info())
    autput_report_name = "report.xlsx"
    df.to_excel(autput_report_name)
    print(f"отчет {autput_report_name}")


def get_coasts_df(excel_file: str) -> pd.DataFrame:
    """
    Формируем новый отчет, в котором будем вычислена итоговая стоимость каждого товара с учетом доставки
    """
    df = pd.read_excel(excel_file)
    df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")
    df.loc[df["Quantity"].isna(), "Quantity"] = [1, 5, 5, 1, 4]
    df.set_index("Date", inplace=True)
    df.drop(columns=["Unnamed: 0"], inplace=True)
    df = df[["Quantity", "Price", "Delivery"]]
    df.rename(columns={
        "Quantity": "Количество",
        "Price": "Цена",
        "Delivery": "Доставка",
    }, inplace=True)
    df["Общая стоимость"] =  df["Количество"] * df["Цена"] + df["Доставка"]
    df["Количество"] = df["Количество"].astype(int)
    df.sort_index(inplace=True)

    return df


if __name__ == "__main__":
    main()
