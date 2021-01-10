import pandas as pd
from ast import literal_eval
import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # or whatever
handler = logging.FileHandler(r"C:\Users\chara\Documents\Data\Interested\meta_data.log", 'w', 'utf-8')  # or whatever
handler.setFormatter(logging.Formatter('%(name)s %(message)s'))  # or whatever
root_logger.addHandler(handler)


def handle_neigh():
    new_df_path = r"C:\Users\chara\Downloads\DF_Processed.csv"
    new_df_path1 = r"C:\Users\chara\Downloads\DF_Processed1.csv"
    df = pd.read_csv(new_df_path)
    df["neighborhood"] = df["('nbh_name', 'nbh_id')"]
    df.drop(columns=["('nbh_name', 'nbh_id')"], inplace=True)
    df.to_csv(new_df_path1, index=False, header=True)
    print("finished")


def apply_nbh_id(input):
    return list(literal_eval(input))[1]


def apply_nbh_name(input):
    return list(literal_eval(input))[0]


def read_data():
    new_df_path1 = r"C:\Users\chara\Documents\Data\All_Data_Nbh_ID\processed.csv"
    new_df_path2 = r"C:\Users\chara\Documents\Data\All_Data_Nbh_ID\processed1.csv"
    df = pd.read_csv(new_df_path1)
    df = df[df["('nbh_name', 'nbh_id')"].notna()]
    print(df["('nbh_name', 'nbh_id')"].isna().sum())
    df['nbh_id'] = df["('nbh_name', 'nbh_id')"].apply(apply_nbh_id)
    df['nbh_name'] = df["('nbh_name', 'nbh_id')"].apply(apply_nbh_name)
    df.drop(columns=["('nbh_name', 'nbh_id')"], inplace=True)
    df.to_csv(new_df_path2, index=False, header=True)


def data_analysis():
    df_path = r"C:\Users\chara\Documents\Data\All_Data_Nbh_ID\processed1.csv"
    data_path_df = pd.read_csv(df_path)
    print(data_path_df)


def read_new_data():
    new_df_path2 = r"C:\Users\chara\Downloads\DF_Processed2.csv"
    df = pd.read_csv(new_df_path2)
    print("finished")


list_neigh = [0, 6, 55, 54, 56, 53, 51, 76, 26, 18, 25, 68, 52, 69, 67, 12, 77, 79, 78, 27]


def extract_interested_neighborhood():
    new_df_path2 = r"C:\Users\chara\Downloads\DF_Processed2.csv"
    new_df_path3 = r"C:\Users\chara\Documents\Data\Interested\Interested_df.csv"
    df = pd.read_csv(new_df_path2)
    list_df = []
    for each in list_neigh:
        each_df = df[df.nbh_id == each]
        list_df.append(each_df)
        root_logger.debug(f' nbh id - {each} - shape - {each_df.shape}')
        path = r"C:\Users\chara\Documents\Data\Interested\{}_neighborhood.csv".format(each)
        each_df.to_csv(path, index=False, header=True)
    interested_df = pd.concat(list_df)
    interested_df.to_csv(new_df_path3, index=False, header=True)
    root_logger.debug(f'Consolidated Debug {interested_df.shape}')


if __name__ == '__main__':
    data_analysis()
