import plotly.graph_objects as go
import plotly.io as pio
from sjvisualizer import PieRace
from sjvisualizer import DataHandler
from sjvisualizer import Canvas, BarRace
import pandas as pd
from data_cleaning import clean_data
from dictionaries import rename_countries_and_cats
import os
import plotly.express as px

df_in_millions = pd.read_csv(
    r"C:\Users\kalot\GitHub\data-science-project\csv_files\csv_in_millions.csv")  # NOQA
df_in_percentages = pd.read_csv(  # already cleaned
    r"C:\Users\kalot\GitHub\data-science-project\csv_files\csv_in_stronger_percentages.csv")  # NOQA

df_in_millions = clean_data(df_in_millions)
df_in_millions = rename_countries_and_cats(df_in_millions)
df_in_millions = df_in_millions.rename(columns={'Year': 'Date'})
df_in_percentages = df_in_percentages.rename(columns={'Year': 'Date'})

# Years should be in DD/MM/YY format for visualization
df_in_percentages['Date'] = '1/1/' + df_in_percentages['Date'].astype(str)
df_in_millions['Date'] = '1/1/' + df_in_millions['Date'].astype(str)


def get_country_dataframe(df: pd.DataFrame, country: str):
    """
    Returns a dataframe for parameter country in sj library format:
    Date        Category1 Category2 ...
    1/1/2012    Value1    Value2    ...
    ...
    """
    grouped = df.groupby('Country')

    # dataframes list has 27 df's each with its own country
    dataframes = []

    # Iterate over the groups and extract each dataset
    for name, group in grouped:
        dataframes.append(group)

    # finding dataframe with param country
    for df in dataframes:
        # Check if the 'Country' column has 'Greece'
        if country in df['Country'].values:
            # Save the DataFrame and exit the loop
            country_dataframe = df
            break
    # deleting country column after finding param dataframe
    country_dataframe = country_dataframe.drop('Country', axis=1)
    df_wide = country_dataframe.pivot_table(index='Date', columns='Category', values='Value')

    # dates goes to agriculture for some reason - splitting the first column entries
    new_df = pd.DataFrame({'Date': df_wide.index, 'Agriculture, forestry, fishing and hunting': df_wide[
        'Agriculture, forestry, fishing and hunting'].values})

    # Convert 'Date' column to datetime type
    new_df['Date'] = new_df['Date'].str.replace('-', '/')
    df_wide.drop('Agriculture, forestry, fishing and hunting', axis=1, inplace=True)

    # Merge the fixed columns to the original DataFrame
    df_new = pd.merge(df_wide, new_df, on='Date')
    df_new['Date'] = pd.to_datetime(df_new['Date'])
    df_new = df_new.drop('Total', axis=1)
    return df_new


def show_pie_chart_distribution_througout_years_of_country(country: str, df=pd.DataFrame):
    df_new = get_country_dataframe(df, 'Greece')

    path = os.getcwd()
    excel_path = os.path.join(path, f'{country}.xlsx')
    if os.path.exists(excel_path):
        # Delete the file
        os.remove(excel_path)
    df_new.to_excel(excel_path, index=False)

    # creating visualization
    file_name = rf'{path}\{country}.xlsx'
    df = DataHandler.DataHandler(excel_file=file_name, number_of_frames=1000).df
    canvas = Canvas.canvas()
    canvas.add_title(f'{country} category expenses between 2012 - 2020')
    canvas.add_time(df=df, time_indicator="year")
    pie_race = PieRace.pie_plot(canvas=canvas.canvas, df=df)
    canvas.add_sub_plot(pie_race)
    canvas.play(fps=60)


def show_bar_category_race_throughout_years_of_country(country, df: pd.DataFrame):
    df_new = get_country_dataframe(df, 'Greece')

    path = os.getcwd()
    excel_path = os.path.join(path, f'{country}.xlsx')
    if os.path.exists(excel_path):
        # Delete the file
        os.remove(excel_path)
    df_new.to_excel(excel_path, index=False)

    # creating visualization
    FPS = 60
    EXCEL_FILE = rf'{path}\{country}.xlsx'
    df = DataHandler.DataHandler(excel_file=EXCEL_FILE, number_of_frames=1000).df
    canvas = Canvas.canvas()
    canvas.add_title(f'{country} category expenses between 2012 - 2020')
    canvas.add_time(df=df, time_indicator="year")
    bar_chart = BarRace.bar_race(canvas=canvas.canvas, df=df, width=1000, height=500)
    canvas.add_sub_plot(bar_chart)
    canvas.play(fps=FPS)


# print(get_country_dataframe(df_in_percentages, 'Greece'))
# print(show_bar_category_race_throughout_years_of_country('Austria', df_in_millions))

def get_country_and_year_dataframe(df:pd.DataFrame, country:str, year:int):
    df = get_country_dataframe(df, country)
    years_and_df_rows = {
        '2012': 0,
        '2013': 1,
        '2014': 2,
        '2015': 3,
        '2016': 4,
        '2017': 5,
        '2018': 6,
        '2019': 7,
        '2020': 8,

    }
    df = df.drop('Date', axis=1)
    return df.iloc[years_and_df_rows[str(year)]]


def create_treemap(df, country, year, perc: bool, PATH):

    series = get_country_and_year_dataframe(df, country, year)
    series = pd.DataFrame({'Category': series.index, 'Value': series.values})
    print(series.head())
    series = series[series['Value'] != 0]

    fig = px.treemap(data_frame=series, path=['Category'], values='Value',
                     color='Value',
                     color_continuous_scale='Magma',
                     hover_data={'Value': ':.2f'},
                     labels={'Value': 'Expense'},
                     title=f'Expense Treemap of {country} in {year}')
    if perc:
        fig.update_traces(hovertemplate='<b>%{label}</b><br>Percentage: %{value:.2f}')
    else:   # millions dataframe
        fig.update_traces(hovertemplate='<b>%{label}</b><br>Millions spent: %{value:.2f}')
    fig.update_layout(
        margin=dict(t=50, l=50, r=50, b=50),
        font=dict(size=18),
        coloraxis_showscale=False)
    fig.write_html(PATH)
    fig.show()
    
print(create_treemap(df_in_percentages, 'Germany', 2013, perc=True, PATH='urpath'))
