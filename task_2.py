from pickle import TRUE
import pandas as pd


def main():
    report_file = "report.xlsx"

    df = pd.read_excel(report_file)
    df.rename(columns={
        "Date": "Дата"
    }, inplace=True)
    df.set_index("Дата", inplace=True)  

    agg_df = get_agg_df(df)
    agg_df.to_excel("agg.xlsx")


def get_agg_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    По предобработанным данным посчитать сумму, среднее и медиану для
    столбцов Количество, Цена, Доставка, Общая стоимость
    """
    agg_df = df.agg({
        "Количество": ["sum", "mean", "median"],
        "Цена": ["mean", "median"],
        "Доставка": ["sum", "mean", "median"],
        "Общая стоимость": ["sum", "mean", "median"]
    })
    agg_df.rename(index={
        "mean": "среднее",
        "median": "медиана",
        "sum": "сумма"
    }, inplace=True)
    agg_df.fillna("-", inplace=True)
    return agg_df


if __name__ == "__main__":
    main()
