import pandas as pd
import matplotlib.pyplot as plt
import os


def save_charts():
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.25)
    file_list = os.listdir('classes/')
    for processed_file in file_list:
        print(f'processing file {processed_file}')
        output_image = 'classlevel_charts/' + processed_file.replace('.txt', '') + "_bar.png"
        df = pd.read_csv('classes/' + processed_file)
        ax = plt.subplot(111)
        ax.bar(df['model_name'], df['map_score'], width=0.5, color='y', align='center')

        # plt.show()
        # plt.figure(figsize=(8, 4))
        plt.xlabel(processed_file.replace('.txt', ''))
        plt.ylabel('class level mAP score')
        plt.savefig(output_image)


if __name__ == '__main__':
    save_charts()
