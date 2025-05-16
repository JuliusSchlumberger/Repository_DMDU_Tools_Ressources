import pandas as pd
from scripts.inputs import (
    CATEGORIES_TOOLS,
    CATEGORIES_RESSOURCES,
    COLORS_TOOLS,
    COLORS_RESSOURCES,
)
from scripts.generate_overview_figure import create_overview_plot
from scripts.generate_tables import generate_table

# # Read the data
df_resources = pd.read_csv("data/form_entries.csv", delimiter=";")
df_tools = pd.read_csv("data/ToolsInput.csv", delimiter=";")
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

df_resource_table = pd.read_csv(
    "data/table_resources.csv", sep=";", encoding="ISO-8859-1"
)
print(df_resource_table)
generate_table(df_resource_table, "resources")
