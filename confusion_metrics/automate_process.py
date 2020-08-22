import pandas as pd

df = pd.read_csv(
    "/home/charan/Documents/research/deep_lite/ResourcesForCharan/Test-Artifacts/test-2017/regular_resnet50/0.5/inference_metrics.csv")

print(len(df.index))

context_map = {
    "anova_resnet50": "context_list.txt",
    "disAnova_resnet50": "disAnova_context_list.txt",
    "co-occurance_resnet50": "cooccurace_context_list.txt",
    "semantic_resnet50": "context_list_semantic.txt"
}

for key in sorted(context_map.keys()):
    print(f'{key} - {context_map[key]}')
