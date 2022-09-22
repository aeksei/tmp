import pandas as pd

from task_1 import get_coasts_df
from task_2 import get_agg_df
from task_3 import get_groupby_df


class ExcelReport:
    """
    Итоговый вариант, который будет содержать себе все 3 варианта сгенерированных отчетов
    и формировать один Excel отчет
    """

    def __init__(self, input_excel: str, output_excel: str):
        self.input_excel = input_excel
        self.output_excel = output_excel

        self.coast_df = self.get_coasts_df()
        self.agg_df = self.get_agg_df()
        self.groupby_df = self.get_groupby_df()

    def get_coasts_df(self) -> pd.DataFrame:
        return get_coasts_df(self.input_excel)

    def get_agg_df(self) -> pd.DataFrame:
        return get_agg_df(self.get_coasts_df())

    def get_groupby_df(self) -> pd.DataFrame:
        return get_groupby_df(self.get_coasts_df())

    def create_report(self):
        with pd.ExcelWriter(self.output_excel) as writer:
            self.coast_df.to_excel(writer, sheet_name="Общая стоимость")
            self.agg_df.to_excel(writer, sheet_name="Сумма, среднее и медиана")
            self.groupby_df.to_excel(writer, sheet_name="Стоимость по каждому месяцу")


if __name__ == "__main__":
    reports = ExcelReport("products.xlsx", "final_report.xlsx")
    reports.create_report()
