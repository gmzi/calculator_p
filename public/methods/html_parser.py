def create_grid(labels_values):
    grid_html = """
    <div style="display: grid; grid-template-columns: auto auto;" class="grid">
    """

    for label, value in labels_values:
        grid_html += f"""
        <div>{label}</div>
        <div>{value}</div>
        """
        
    # Close the grid HTML markup
    grid_html += """
    </div>
    """
    return grid_html

def footer_html():
    footer_html = """
    <div style="margin-top: 20px;">
      <hr />
      <p>NOTES:</p>
      <ul class="notes-list">
        <li>-- all fields account for reinvestments --</li>
        <li>[*]: TD calls it "Discount".</li>
        <li>[**]: TD calls it "Yield".</li>
      </ul>
    </div>
    """
    return footer_html

def create_grid_maturity(labels_values):
    grid_html = """
    <div style="display: grid; grid-template-columns: auto auto;" class="grid">
    """
    for label, value in labels_values:
        if label == "Maturity date:":
            grid_html += f"""
            <div>{label}</div>
            <div id="maturity-date">{value}</div>
            """
        else:
            grid_html += f"""
            <div>{label}</div>
            <div>{value}</div>
            """

    grid_html += """</div>"""
    return grid_html

def balances_grid(dict_):
    grid_html = """
    <h5>total income by year</h5>
    <div style="display: grid; grid-template-columns: auto auto;" class="grid">
    """
    for key, value in dict_.items():
        grid_html += f"""
        <div>{key}</div>
        <div>{value}</div>
        """
    grid_html += """
    </div>
    """
    return grid_html