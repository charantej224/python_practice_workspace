import os
import pandas as pd

inferences_path = "/home/charan/Documents/research/deep_lite/ResourcesForCharan/Test-Artifacts/test-2017"
inside_path = "0.8/inference_metrics.csv"
key = "yolo"

for each in os.listdir(inferences_path):
    if key in each:
        path_to_read = os.path.join(inferences_path, each, inside_path)
        data_frame = pd.read_csv(path_to_read)
        data_frame = data_frame.sort_values("image_id")
        data_frame.to_csv(each + ".csv", index=False)
