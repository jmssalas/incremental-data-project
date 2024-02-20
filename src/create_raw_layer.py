import pandas as pd
import json


def create_raw_layer(sql_con, table_by_platform, raw_table) -> None:
    raw_layer_list = []
    for platform, table in table_by_platform.items():
        print("Reading", table, "...")
        df = pd.read_sql_query("SELECT * FROM " + table, sql_con)
        for _, row in df.iterrows():
            data = json.loads(row._airbyte_data)
            data["platform"] = platform
            raw_layer_list.append(data)

    print("Total:", len(raw_layer_list))

    print("Storing into sqlite...")
    pd.DataFrame(raw_layer_list).to_sql(raw_table,
                                        sql_con,
                                        if_exists="replace")
    print("Done")
