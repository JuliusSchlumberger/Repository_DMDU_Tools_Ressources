import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import numpy as np
from datetime import datetime
from scripts.helper_functions import (
    add_linebreaks,
    HandlerPatchWithDot,
    turn_df_numeric_for_heatmap,
)


def create_overview_plot(
    categories: dict, colors: dict, split_by: str, relevant_table, fname: str
):
    # Create a mapping of columns to colors
    column_colors = {}
    for category, columns in categories.items():
        for column in columns:
            column_colors[column] = colors[category]

    x_labels = [item for sublist in categories.values() for item in sublist]

    # Sort the DataFrame alphabetically by Sector and reset the index
    relevant_table = relevant_table.drop(
        columns=[
            "Name.1",
            "Do you " "want to submit " "a tool or a " "resource?",
            "Link",
        ]
    )
    relevant_table["Accessibility"] = relevant_table["Accessibility"].astype(str).str[0]
    df = relevant_table.sort_values(by=split_by).reset_index(drop=True)

    # Get unique subplot-labels
    unique_subplot_names = df[split_by].unique()

    # Prepare for plotting
    if fname == "resources":
        # x_labels = df.columns[2:-1]  # Exclude the 'Author' and 'Sector' columns
        df["Case study"] = df["Case study"].replace(
            "no, it does not contain any information from a case study.", np.nan
        )
    # elif fname == 'tools':
    #     # x_labels = df.columns[2:].drop(df.columns[-2])

    # Relative subplot heights based on the number of rows per sector group
    unique_subplot_names_counts = df[split_by].value_counts(sort=False)
    relative_heights = unique_subplot_names_counts / unique_subplot_names_counts.sum()

    # Create subplots
    fig, axes = plt.subplots(
        nrows=len(unique_subplot_names),
        ncols=1,
        figsize=(14, 12),
        gridspec_kw={"height_ratios": relative_heights},
    )

    if len(unique_subplot_names) == 1:
        axes = [axes]  # Ensure axes is iterable when there's only one subplot

    # Define colormap
    # Extract heatmap background colors from COLORS
    heatmap_colors = [color_pair[1] for color_pair in colors.values()]

    # Define colormap and normalization
    cmap = mcolors.ListedColormap(heatmap_colors)
    bounds = np.arange(len(heatmap_colors) + 1) - 0.5
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    # Plot each sector group
    for ax, unique_subplot in zip(axes, unique_subplot_names):
        subplot_df = df[df[split_by] == unique_subplot]
        subplot_df = subplot_df.sort_values(
            by=["Accessibility", "Name"], ascending=False
        ).reset_index(drop=True)
        authors = subplot_df["Name"]
        subplot_df_reordered = subplot_df[x_labels]
        # subplot_df = subplot_df.drop(columns = ['Name', split_by])

        df_numeric = turn_df_numeric_for_heatmap(
            subplot_df_reordered, categories
        ).astype(int)

        df_numeric.set_index(authors)

        sns.heatmap(
            df_numeric,
            annot=False,
            cmap=cmap,
            norm=norm,
            ax=ax,
            cbar=False,
            linewidths=0.5,
            linecolor="white",
        )

        for i, author in enumerate(authors):
            for column in x_labels:
                if subplot_df_reordered.at[subplot_df_reordered.index[i], column] in [
                    "extensive " "coverage",
                    "yes, it provides an extensive illustration of a case study.",
                ]:
                    ax.plot(
                        x_labels.index(column) + 0.5,  # x-coordinate
                        i + 0.5,  # y-coordinate
                        marker="o",  # Marker style (circle in this case)
                        label=column,  # Label for legend
                        color=column_colors[column][0],  # Marker color
                        markersize=10,  # Marker size
                    )
                elif subplot_df_reordered.at[subplot_df_reordered.index[i], column] in [
                    "some " "coverage",
                    "yes, it provides some shot examples from a case study.",
                ]:
                    ax.plot(
                        x_labels.index(column) + 0.5,  # x-coordinate
                        i + 0.5,  # y-coordinate
                        marker="o",  # Marker style
                        fillstyle="left",  # Fill style (left half filled)
                        label=column,  # Label for legend
                        color=column_colors[column][0],  # Marker color
                        markersize=10,  # Marker size
                    )
                elif (
                    isinstance(
                        subplot_df_reordered.at[subplot_df_reordered.index[i], column],
                        str,
                    )
                    and subplot_df_reordered.at[subplot_df_reordered.index[i], column]
                    != "no coverage"
                ):
                    corr = 0.15
                    accessibility_text = subplot_df_reordered.at[
                        subplot_df_reordered.index[i], column
                    ]
                    ax.annotate(
                        accessibility_text,
                        xy=(x_labels.index(column) - corr + 0.5, i + 0.5 + corr),
                        fontsize=12,
                        fontweight="bold",
                    )

        # Customize each subplot
        ax.set_yticks(np.arange(len(authors)) + 0.5)
        ax.set_yticklabels(authors, rotation=0, fontsize=12)
        ax.set_ylabel(
            add_linebreaks(unique_subplot, 15),
            rotation=0,
            labelpad=10,
            fontsize=14,
            va="center",
            ha="right",
        )

        # ax.yaxis.set_label_position("right")
        ax.yaxis.set_label_position("left")
        ax.yaxis.tick_right()
        # Extend y-limits slightly to ensure markers fit
        # ax.set_ylim(-0.5, len(authors) + 0.5)
        ax.set_xlim(-0.1, len(x_labels))

        # Remove unwanted spines
        ax.spines["top"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["right"].set_visible(True)
        ax.spines["left"].set_visible(True)

        # Show x-tick labels only on the last subplot
        if ax != axes[0]:
            ax.set_xticklabels([])
            ax.set_xticks([])
        else:
            ax.set_xticks(np.arange(len(x_labels)) + 0.5)
            ax.set_xticklabels(
                x_labels, rotation=45, ha="left", rotation_mode="anchor", fontsize=12
            )
            ax.xaxis.tick_top()

    # Adjust subplot spacing and margins to fit labels
    plt.subplots_adjust(left=0.25, right=0.9, top=0.95, bottom=0.1, hspace=0.6)

    # Create combined handles (as dicts) for legend
    legend_handles = []
    for idx, (category, color) in enumerate(colors.items()):
        combined = {"facecolor": color[1], "markercolor": color[0]}
        if category.capitalize() == "Accessibility":
            category = "Accessibility*"
        legend_handles.append((combined, category.capitalize()))

    if len(legend_handles) % 2 != 0:
        legend_handles += [
            (
                {"facecolor": "white", "markercolor": "white", "fillstyle": "left"},
                add_linebreaks("", 45),
            )
        ]

    # Add special entries for coverage levels
    if split_by == "Language":
        legend_handles += [
            (
                {"facecolor": "#D3D3D3", "markercolor": "#4d4d4d", "fillstyle": "left"},
                "Can be partially completed",
            ),
            (
                {"facecolor": "#D3D3D3", "markercolor": "#4d4d4d", "fillstyle": "full"},
                "Can be completed independently",
            ),
        ]
    else:
        legend_handles += [
            (
                {"facecolor": "#D3D3D3", "markercolor": "#4d4d4d", "fillstyle": "left"},
                "Some Coverage",
            ),
            (
                {"facecolor": "#D3D3D3", "markercolor": "#4d4d4d", "fillstyle": "full"},
                "Extensive Coverage",
            ),
        ]

    legend_handles += [
        (
            {"facecolor": "white", "markercolor": "white", "fillstyle": "left"},
            add_linebreaks("", 45),
        )
    ]

    # Build the legend
    plt.legend(
        [h[0] for h in legend_handles],
        [h[1] for h in legend_handles],
        ncol=5,
        title="Legend",
        alignment="left",
        title_fontsize=14,
        handler_map={dict: HandlerPatchWithDot(scale_height=2)},
        bbox_to_anchor=(-0.2, 0.01),
        loc="upper left",
        fontsize=12,
        labelspacing=1.1,  # space between items
        handlelength=2,  # space allocated for marker
        handletextpad=1.5,  # spacing between marker and text
        borderpad=2.5,  # Increased padding inside the legend box
    )
    if split_by == "Language":
        plt.figtext(
            0.07,
            0.02,
            "*A: no prior coding experience required, B: basic coding "
            "experience required",
            ha="left",
            fontsize=12,
            color="black",
        )
    else:
        plt.figtext(
            0.07,
            0.02,
            "*A: suited for beginners, B: some knowledge required, "
            "C: targeted towards analysts.",
            ha="left",
            fontsize=12,
            color="black",
        )

    timestamp = datetime.now().strftime("Last Updated: %Y-%m-%d %H:%M")
    plt.figtext(0.99, 0.005, timestamp, ha="right", fontsize=8, color="gray")

    plt.tight_layout()
    plt.savefig(f"figures/overview_{fname}.png", dpi=300)
    # plt.show()
