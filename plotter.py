import pandas as pd

df = pd.read_csv("log.csv", parse_dates=[0])

html = df.to_html(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', 
formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, bold_rows=True, 
classes=None, escape=True, max_rows=None, max_cols=None, show_dimensions=False, notebook=False, decimal='.', 
border=None, table_id=None)

print(html)
