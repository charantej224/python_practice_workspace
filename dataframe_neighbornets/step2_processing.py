import pandas as pd
import re
import logging

df_path = r"C:\Users\chara\Downloads\311_neighborhood.csv"
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # or whatever
handler = logging.FileHandler(r"C:\Users\chara\Documents\Data\Step2\9\meta_data.log", 'w',
                              'utf-8')  # or whatever
handler.setFormatter(logging.Formatter('%(message)s'))  # or whatever
root_logger.addHandler(handler)


def step2(data_311):
    list_years = sorted(list(data_311["CREATION YEAR"].unique()))
    list_months = sorted(list(data_311["CREATION MONTH"].unique()))
    root_logger.debug("********** Step - 2 ************************")
    for year in list_years:
        for month in list_months:
            each_df = data_311[data_311["CREATION YEAR"] == year]
            each_df = each_df[each_df["CREATION MONTH"] == month]
            each_path = r"C:\Users\chara\Documents\Data\Step2\9\2\{}_year_{}_month.csv".format(year, month)
            root_logger.debug(f'Year - {year} Month - {month} - Shape - {each_df.shape}')
            each_df.to_csv(each_path, header=True, index=False)


def step3(year, data_311):
    list_channels = list(data_311["SOURCE"].unique())
    root_logger.debug("********** Step - 3 ************************")
    for channel in list_channels:
        each_df = data_311[data_311["SOURCE"] == channel]
        each_path = r"C:\Users\chara\Documents\Data\Step2\9\3\{}_{}_source.csv".format(year, channel)
        root_logger.debug(f'Year - {year} Source {channel} - Shape {each_df.shape}')
        each_df.to_csv(each_path, header=True, index=False)


def step4(year, data_311):
    column = "NEIGHBORHOOD"
    list_vals = list(data_311[column].unique())
    root_logger.debug("********** Step - 4 ************************")
    for val in list_vals:
        each_df = data_311[data_311[column] == val]
        val = re.sub('[^A-Za-z0-9]+', '-', str(val))
        each_path = r"C:\Users\chara\Documents\Data\Step2\9\4\{}_{}_{}.csv".format(year, val, column)
        root_logger.debug(f'Year - {year} Neighborhood {val} - Shape {each_df.shape}')
        each_df.to_csv(each_path, header=True, index=False)


def step5(year, data_311):
    column = "CATEGORY"
    list_vals = list(data_311[column].unique())
    root_logger.debug("********** Step - 5 ************************")
    for val in list_vals:
        each_df = data_311[data_311[column] == val]
        val = re.sub('[^A-Za-z0-9]+', '-', str(val))
        each_path = r"C:\Users\chara\Documents\Data\Step2\9\5\{}_{}_{}.csv".format(year, val, column)
        root_logger.debug(f'Year - {year} Category {val} - Shape {each_df.shape}')
        each_df.to_csv(each_path, header=True, index=False)


def step6(year, data_311):
    column = "TYPE"
    list_vals = list(data_311[column].unique())
    root_logger.debug("********** Step - 6 ************************")
    for val in list_vals:
        each_df = data_311[data_311[column] == val]
        val = re.sub('[^A-Za-z0-9]+', '-', str(val))
        each_path = r"C:\Users\chara\Documents\Data\Step2\9\6\{}_{}_{}.csv".format(year, val, column)
        root_logger.debug(f'Year - {year} - {column.lower()} - {val} - Shape {each_df.shape}')
        each_df.to_csv(each_path, header=True, index=False)


def step7(year, data_311):
    column = "DEPARTMENT"
    list_vals = list(data_311[column].unique())
    root_logger.debug("********** Step - 7 ************************")
    for val in list_vals:
        each_df = data_311[data_311[column] == val]
        val = re.sub('[^A-Za-z0-9]+', '-', str(val))
        each_path = r"C:\Users\chara\Documents\Data\Step2\9\7\{}_{}_{}.csv".format(year, val, column)
        root_logger.debug(f'Year - {year}  - {column.lower()} - {val} - Shape {each_df.shape}')
        each_df.to_csv(each_path, header=True, index=False)


def step8(year, data_311):
    root_logger.debug("********** Step - 8 ************************")
    filtered_df = data_311[data_311['DAYS TO CLOSE'].notnull()]
    filtered_df["DAYS TO CLOSE"] = filtered_df["DAYS TO CLOSE"].astype('int64')
    df_day = filtered_df[filtered_df["DAYS TO CLOSE"] == 1]
    df_week = filtered_df[1 < filtered_df["DAYS TO CLOSE"]]
    df_week = df_week[df_week["DAYS TO CLOSE"] < 8]
    df_two_week = filtered_df[7 < filtered_df["DAYS TO CLOSE"]]
    df_two_week = df_two_week[df_two_week["DAYS TO CLOSE"] < 15]
    df_two_week_more = filtered_df[filtered_df["DAYS TO CLOSE"] > 14]
    df_day_path = r"C:\Users\chara\Documents\Data\Step2\9\8\{}_days_{}.csv".format(year, "one_day")
    df_week_path = r"C:\Users\chara\Documents\Data\Step2\9\8\{}_days_{}.csv".format(year, "week")
    df_two_week_path = r"C:\Users\chara\Documents\Data\Step2\9\8\{}_days_{}.csv".format(year, "two_weeks")
    df_two_week_more_path = r"C:\Users\chara\Documents\Data\Step2\9\8\{}_days_{}.csv".format(year,"more_than_two_weeks")
    df_day.to_csv(df_day_path, header=True, index=False)
    df_week.to_csv(df_week_path, header=True, index=False)
    df_two_week.to_csv(df_two_week_path, header=True, index=False)
    df_two_week_more.to_csv(df_two_week_more_path, header=True, index=False)
    root_logger.debug(f'Year - {year} - One day - Shape {df_day.shape}')
    root_logger.debug(f'Year - {year} - One Week - Shape {df_week.shape}')
    root_logger.debug(f'Year - {year} - two weeks - Shape {df_two_week.shape}')
    root_logger.debug(f'Year - {year} - more than two weeks - Shape {df_two_week_more.shape}')


if __name__ == '__main__':
    original_data_311 = pd.read_csv(df_path)
    list_years = sorted(list(original_data_311["CREATION YEAR"].unique()))
    for each in list_years:
        root_logger.debug(f'Year in Process {each}')
        in_data_311 = original_data_311[original_data_311["CREATION YEAR"] == each]
        step2(in_data_311)

    for each in list_years:
        root_logger.debug(f'Year in Process {each}')
        in_data_311 = original_data_311[original_data_311["CREATION YEAR"] == each]
        step3(each, in_data_311)

    for each in list_years:
        root_logger.debug(f'Year in Process {each}')
        in_data_311 = original_data_311[original_data_311["CREATION YEAR"] == each]
        step4(each, in_data_311)

    for each in list_years:
        root_logger.debug(f'Year in Process {each}')
        in_data_311 = original_data_311[original_data_311["CREATION YEAR"] == each]
        step5(each, in_data_311)

    for each in list_years:
        root_logger.debug(f'Year in Process {each}')
        in_data_311 = original_data_311[original_data_311["CREATION YEAR"] == each]
        step6(each, in_data_311)

    for each in list_years:
        root_logger.debug(f'Year in Process {each}')
        in_data_311 = original_data_311[original_data_311["CREATION YEAR"] == each]
        step7(each, in_data_311)

    for each in list_years:
        root_logger.debug(f'Year in Process {each}')
        in_data_311 = original_data_311[original_data_311["CREATION YEAR"] == each]
        step8(each, in_data_311)
