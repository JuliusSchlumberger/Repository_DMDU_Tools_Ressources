def generate_table(df, table_group="resources"):
    output_path = f"outputs/table_{table_group}.html"
    # Generate HTML table
    html_content = """
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Link</th>
            </tr>
        </thead>
        <tbody>
    """

    # Append rows from DataFrame
    for _, row in df.iterrows():
        html_content += f"""
            <tr>
                <td>{row['Authors']}</td>
                <td>{row['Short description (shortened)']}</td>
                <td><a href="{row['Link']}" target="_blank">Link</a></td>
            </tr>
        """
    html_content += """
        </tbody>
    </table>
    """

    # Save to file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
