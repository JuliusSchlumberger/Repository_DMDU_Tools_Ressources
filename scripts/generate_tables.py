def generate_table(df, table_group="resources"):
    output_path = f"outputs/table_{table_group}.html"

    # Generate HTML table with styling
    html_content = """
    <html>
    <head>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 1rem;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            th, td {
                border: 1px solid #999;
                padding: 0.5rem;
                text-align: left;
            }
            th {
                background-color: #eee;
            }
        </style>
    </head>
    <body>
    <table>
        <thead>
            <tr>
                <th style="width: 20%;">Name</th>
                <th style="width: 60%;">Description</th>
                <th style="width: 20%;">Link</th>
            </tr>
        </thead>
        <tbody>
    """
    df = df.sort_values(by="Authors")

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
    </body>
    </html>
    """

    # Save to file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
