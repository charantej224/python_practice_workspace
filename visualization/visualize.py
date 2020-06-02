import pandas as pd
import matplotlib.pyplot as plt
import os


def save_charts():
    plt.xticks(rotation=90)
    file_list = os.listdir('outputs/')
    for processed_file in file_list:
        output_image = 'charts/' + processed_file.replace('_output.txt', '') + "_bar.png"
        df = pd.read_csv('outputs/' + processed_file)
        ax = plt.subplot(111)
        ax.bar(df['class_name'], df['mAP'], width=0.5, color='b', align='center')


        # plt.show()
        # plt.figure(figsize=(8, 4))
        plt.savefig(output_image)


def process_files(input_list):
    for each_input in input_list:
        processed_output = []
        file_name = 'inputs/' + each_input + '.txt'
        file_output = 'outputs/' + each_input + '_output.txt'

        with open(file_name, 'r') as f:
            data = f.readlines()
            f.close()
        for each_line in data:
            if not (each_line.startswith('NEW MIN') or each_line.startswith('mAP')):
                split_data = each_line.split('=')
                processed_output.append(
                    split_data[1].replace('AP', '').strip() + ',' + split_data[0].replace('%', '').strip())
        with open(file_output, 'w') as f:
            f.write('class_name,mAP\n')
            f.write("\n".join(processed_output))
            f.close()


def read_inputs():
    input_files = os.listdir('inputs/')
    input_files = [each.replace('.txt', '') for each in input_files]
    return input_files


if __name__ == '__main__':
    read_input_list = read_inputs()
    print(read_input_list)
    process_files(read_input_list)
    print('files processed, check output directory')
    save_charts()
    print('finished charts. fuck yoU!')
