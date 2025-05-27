def preprocess(df, unique_tools_column, unqiue_resource_columns, renaming_dict):
    print(df.to_string())
    df_resources = df[
        df["Do you want to submit a tool or a resource?"]
        == "I want to submit a resource"
    ]
    df_tools = df[
        df["Do you want to submit a tool or a resource?"] == "I want to submit a tool"
    ]

    # Identify relevant columns
    tools_columns = unique_tools_column + [col for col in df.columns if "tool" in col]
    resource_columns = unqiue_resource_columns + [
        col for col in df.columns if "resource" in col
    ]

    df_tools = df_tools[tools_columns]
    df_resources = df_resources[resource_columns]

    # Rename columns
    df_tools = df_tools.rename(columns=renaming_dict)
    df_resources = df_resources.rename(columns=renaming_dict)

    df_tools.to_csv("data/tools_table.csv", sep="\t", index=False)
    df_resources.to_csv("data/resources_table.csv", sep="\t", index=False)
