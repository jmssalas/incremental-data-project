import pandas as pd
import json

def create_raw_layer(sqlCon, tableByPlatform, rawTable) -> None:
    raw_layer_list = []
    for platform, table in tableByPlatform.items(): 
        print("Reading", table, "...")
        df = pd.read_sql_query("SELECT * FROM " + table, sqlCon)
        for _, row in df.iterrows():
            data = json.loads(row._airbyte_data)
            data["platform"] = platform
            raw_layer_list.append(data)
    
    print("Total:", len(raw_layer_list))

    print("Storing into sqlite...")
    pd.DataFrame(raw_layer_list).to_sql(rawTable, sqlCon, if_exists="replace")
    print("Done")
