import pandas as pd
from scripts.inputs import (
    CATEGORIES_TOOLS,
    CATEGORIES_RESSOURCES,
    COLORS_TOOLS,
    COLORS_RESSOURCES,
    RENAMING_DICT,
    UNIQUE_TOOLS_COLUMNS,
    UNIQUE_RESOURCE_COLUMNS,
)
from scripts.generate_overview_figure import create_overview_plot
from scripts.preprocess_data import preprocess
from scripts.generate_tables import generate_table

# Preporcess data
df = pd.read_csv("data/form_entries.csv")
preprocess(df, UNIQUE_TOOLS_COLUMNS, UNIQUE_RESOURCE_COLUMNS, RENAMING_DICT)

# # Read the data
df_resources = pd.read_csv("data/resources_table.csv", sep="\t")
df_tools = pd.read_csv("data/tools_table.csv", sep="\t")
# print(df_resources)
create_overview_plot(
    categories=CATEGORIES_RESSOURCES,
    colors=COLORS_RESSOURCES,
    split_by="Sector",
    relevant_table=df_resources,
    fname="resources",
)
# print(df_tools)
create_overview_plot(
    categories=CATEGORIES_TOOLS,
    colors=COLORS_TOOLS,
    split_by="Language",
    relevant_table=df_tools,
    fname="tools",
)

generate_table(df_resources, "resources")
generate_table(df_tools, "tools")
