import pandas as pd
import os
import shutil


# Collect 100 images into text.
def collect_image_ids():
    inference_df = pd.read_csv("inference_metrics_yolo_416_anova.csv")
    image_series = inference_df[0:101]["image_id"].tolist()
    image_string = "\n".join(image_series)

    with open("image_100.txt", "w") as f:
        f.write(image_string)
        f.close()


def read_file_as_list():
    with open("image_100.txt", "r") as f:
        image_list = f.readlines()
        f.close()
    image_list = [each.strip() for each in image_list]
    return image_list


def extract_images():
    path_to_write = "/home/charan/Documents/research/deep_lite/100_images/"
    source_folder = "/home/charan/Documents/research/deep_lite/New_Resources/Test-Artifacts/test-2017/"
    key = "yolo"
    images_100 = read_file_as_list()
    string_list = os.listdir(source_folder)
    final_list = []
    for each in string_list:
        if key in each:
            final_list.append(each)
            path_to_extract = os.path.join(source_folder, each, "0.8/output")
            path_with_directory = os.path.join(path_to_write, each)
            if not os.path.exists(path_with_directory):
                os.makedirs(path_with_directory, exist_ok=True)
            for each_image in images_100:
                source_image_path = os.path.join(path_to_extract, each_image)
                dest_image_path = os.path.join(path_with_directory, each_image)
                shutil.copyfile(source_image_path, dest_image_path)


if __name__ == "__main__":
    extract_images()
