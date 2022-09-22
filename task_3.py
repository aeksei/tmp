import pandas as pd


def main():
    report_file = "report.xlsx"

    df = pd.read_excel(report_file)
    df.rename(columns={
        "Date": "Дата"
    }, inplace=True)
    df.set_index("Дата", inplace=True)
    df.info()

    groupby_df = get_groupby_df(df)
    groupby_df.to_excel("groupby_month.xlsx")


def get_groupby_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Сгруппировать данные по месяцам и посчитать количество товаров по каждому месяцу и
    среднюю и общую стоимость за каждый месяц
    """
    grby_df = df.groupby(pd.Grouper(freq="1M")).agg({
        "Количество": "sum",
        "Общая стоимость": ["sum", "mean"]
    })
    grby_df.rename(columns={
        "sum": "Итого",
        "mean": "Среднее"
    }, inplace=True)
    return grby_df


if __name__ == "__main__":
    main()
