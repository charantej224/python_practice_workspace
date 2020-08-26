import os
import ast

current_dir = "/home/charan/Documents/research/deep_lite/ResourcesForCharan/"
context = "cooccurace_context_list.txt"
with open(os.path.join(current_dir, context), 'r') as f:
    ctx_list = ast.literal_eval(f.readlines()[0])
print(ctx_list)
