def detect_numeric_columns(df):
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    return numeric_cols


def make_chart_data(df):
    chart_list = []

    numeric_cols  = detect_numeric_columns(df)

    #For each numeric column, create a chart dataset
    for col in numeric_cols:
        chart_list.append({
            "title": f"{col} Overview",
            "labels": df.indec.tolist(),
            "values": df[col].fillna(0).tolist(),
        })

        return chart_list
    