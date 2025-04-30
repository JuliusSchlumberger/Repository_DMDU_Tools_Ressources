import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors
import seaborn as sns
import numpy as np

from scripts.inputs_ressources import CATEGORIES, COLORS

def turn_df_numeric_for_heatmap(df, col_dict):
    updated_df = df.copy()
    col_index = 0
    for i, (key, items) in enumerate(col_dict.items()):
        num_cols = len(items)
        for _ in range(num_cols):
            if col_index < len(updated_df.columns):
                updated_df.iloc[:, col_index] = i
                col_index += 1
            else:
                break  # Stop if we run out of columns
    return updated_df

# Create a mapping of columns to colors
column_colors = {}
for category, columns in CATEGORIES.items():
    for column in columns:
        column_colors[column] = COLORS[category]

# Read the data
df = pd.read_csv('data/form_entries.csv')

# Sort the DataFrame alphabetically by Sector and reset the index
df = df.sort_values(by='Sector').reset_index(drop=True)

# Get unique sectors
sectors = df['Sector'].unique()

# Prepare for plotting
x_labels = df.columns[:-2]  # Exclude the 'Author' and 'Sector' columns

# Calculate relative subplot heights based on the number of rows in each sector group
sector_counts = df['Sector'].value_counts(sort=False)
relative_heights = sector_counts / sector_counts.sum()


def add_linebreaks(text, max_length=12):
    """
    Adds line breaks to a string by replacing the next whitespace after `max_length` characters.

    Parameters:
        text (str): The input string.
        max_length (int): The maximum number of characters before a line break (default is 12).

    Returns:
        str: The modified string with line breaks.
    """
    result = ""
    while len(text) > max_length:
        # Find the position of the next whitespace after max_length
        split_pos = text[:max_length].rfind(" ")
        if split_pos == -1:  # If no space is found, break at max_length
            split_pos = max_length
        else:
            split_pos += 1  # Include the whitespace in the split

        # Append the substring and a newline
        result += text[:split_pos] + "\n"
        text = text[split_pos:]  # Update the text to the remaining part

    # Add the remainder of the string
    result += text
    return result


# Create subplots
fig, axes = plt.subplots(
    nrows=len(sectors),
    ncols=1,
    figsize=(14, 12),
    gridspec_kw={'height_ratios': relative_heights}
)

if len(sectors) == 1:
    axes = [axes]  # Ensure axes is iterable when there's only one subplot

# Define colormap
light_colors = ['#D3D3D3', '#FFE0B3', '#CCE0FF','#CCFFCC','#FFCCCC','#E0CCFF',  ]

cmap = mcolors.ListedColormap(light_colors)
bounds = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
norm = mcolors.BoundaryNorm(bounds, cmap.N)

# Plot each sector group
for ax, sector in zip(axes, sectors):
    sector_df = df[df['Sector'] == sector]
    sector_df = sector_df.sort_values(by=['Accessibility', 'Author'], ascending=False).reset_index(drop=True)
    authors = sector_df['Author']

    df_numeric = turn_df_numeric_for_heatmap(sector_df[x_labels], CATEGORIES).astype(int)
    df_numeric.index = authors

    sns.heatmap(df_numeric, annot=False, cmap=cmap, norm=norm, ax=ax, cbar=False,
                linewidths=0.5, linecolor='white')

    # plt.show()
    # print(error)

    for i, author in enumerate(authors):
        for column in x_labels:
            if sector_df.at[sector_df.index[i], column] == 1:
                ax.plot(
                    x_labels.get_loc(column)+0.5,  # x-coordinate
                    i+0.5,  # y-coordinate
                    marker='o',  # Marker style (circle in this case)
                    label=column,  # Label for legend
                    color=column_colors[column],  # Marker color
                    markersize=10  # Marker size
                )
            elif sector_df.at[sector_df.index[i], column] == -1:
                ax.plot(
                    x_labels.get_loc(column)+0.5,  # x-coordinate
                    i+0.5,  # y-coordinate
                    marker='o',  # Marker style
                    fillstyle='left',  # Fill style (left half filled)
                    label=column,  # Label for legend
                    color=column_colors[column],  # Marker color
                    markersize=10  # Marker size
                )
            elif isinstance(sector_df.at[sector_df.index[i], column], str):
                corr = 0.15
                accessibility_text = sector_df.at[sector_df.index[i], column]
                ax.annotate(accessibility_text, xy=(x_labels.get_loc(column) - corr + 0.5,
                                                    i+0.5+corr),
                            fontsize=12, fontweight='bold')

    # Customize each subplot
    ax.set_yticks(np.arange(len(authors)) + 0.5)
    ax.set_yticklabels(authors, rotation=0,fontsize=12)
    ax.set_ylabel(add_linebreaks(sector,15), rotation=0, labelpad=10, fontsize=14, va='center',
                  ha='right')

    # ax.yaxis.set_label_position("right")
    ax.yaxis.set_label_position("left")
    ax.yaxis.tick_right()
    # Extend y-limits slightly to ensure markers fit
    # ax.set_ylim(-0.5, len(authors) + 0.5)
    ax.set_xlim(-.1, len(x_labels))

    # Remove unwanted spines
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(True)
    ax.spines['left'].set_visible(True)

    # Show x-tick labels only on the last subplot
    if ax != axes[0]:
        ax.set_xticklabels([])
        ax.set_xticks([])
    else:
        ax.set_xticks(np.arange(len(x_labels)) + 0.5)
        ax.set_xticklabels(x_labels, rotation=45,
                  ha='left', rotation_mode='anchor', fontsize=12)
        ax.xaxis.tick_top()

# Add a shared x-axis label
# fig.text(0.5, 0.95, 'Criteria', ha='center', fontsize=12)

# Adjust subplot spacing and margins to fit labels
plt.subplots_adjust(left=0.25, right=0.9, top=0.95, bottom=0.1, hspace=0.6)

# Add a shared legend
handles = [plt.Line2D([0], [0], marker='o', color=color, linestyle='None', markersize=10, label=category)
           for category, color in COLORS.items()]
fig.legend(handles=handles, title="Categories", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig('figures/overview.png', dpi=300)
# plt.show()
