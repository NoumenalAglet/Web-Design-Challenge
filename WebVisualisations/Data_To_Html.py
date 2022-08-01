# Import dependencies
import pandas as pd

# Read the csv file
cities_df = pd.read_csv('./Resources/cities.csv')

# Output to Cities_Data.html in table format, which will then be added to Data.html for display
cities_df.to_html('Cities_Data.html', classes=['table', 'table-striped', 'table-hover'])