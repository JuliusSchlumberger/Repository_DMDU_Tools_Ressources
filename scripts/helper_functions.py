from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerBase


# Custom handler that draws a marker on top of a patch
class HandlerPatchWithDot(HandlerBase):
    def __init__(self, scale_height=1.5, **kwargs):
        self.scale_width = scale_height * 0.6
        self.scale_height = scale_height
        super().__init__(**kwargs)

    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ):
        scaled_width = width * self.scale_width
        scaled_height = height * self.scale_height

        # Background patch
        patch = Rectangle(
            (xdescent, ydescent - (scaled_height - height) / 2),
            scaled_width,
            scaled_height,
            facecolor=orig_handle["facecolor"],
            edgecolor=orig_handle["markercolor"],
            transform=trans,
        )

        # Marker
        marker = Line2D(
            [xdescent + scaled_width / 2],
            [ydescent + height / 2],
            marker="o",
            color=orig_handle["markercolor"],
            fillstyle=orig_handle.get("fillstyle", "full"),
            linestyle="None",
            markersize=8 * self.scale_height * 0.65,
            transform=trans,
        )

        return [patch, marker]


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


def add_linebreaks(text, max_length=12):
    """
    Adds line breaks to a string by replacing the next whitespace after
    `max_length` characters.

    Parameters:
        text (str): The input string.
        max_length (int): The maximum number of characters before a line break
                          (default is 12).

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
