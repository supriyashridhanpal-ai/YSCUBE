import os
import csv


class StudyGraph:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self.data = {}

    def build(self, cut: int | None = None) -> dict:
        if not os.path.exists(self.data_dir):
            print(f"Data directory not found: {self.data_dir}")
            return self.data

        for filename in os.listdir(self.data_dir):
            if not filename.endswith(".csv"):
                continue

            filepath = os.path.join(self.data_dir, filename)
            table_name = filename.replace(".csv", "")

            try:
                with open(filepath, "r", encoding="utf-8-sig") as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)

                    if cut:
                        rows = rows[:cut]

                    self.data[table_name] = rows

            except Exception as e:
                print(f"Error loading {filename}: {e}")

        return self.data

    def patient360(self, usubjid: str) -> dict:
        result = {
            "USUBJID": usubjid,
            "visits": [],
            "labs": [],
            "adverse_events": [],
            "doses": [],
            "medicines": [],
            "history": [],
            "disposition": []
        }

        for table_name, rows in self.data.items():
            for row in rows:
                if row.get("USUBJID") == usubjid:
                    if table_name in result:
                        result[table_name].append(row)

        return result
