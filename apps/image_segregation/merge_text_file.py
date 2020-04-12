import os

final_inference = "final_inference.txt"
final_data = ""
folder = "/home/charan/Downloads/drive-download-20200402T192634Z-001/"
for file in sorted(os.listdir(folder)):
    print(file)
    file_path = os.path.join(folder, file)
    f = open(file_path, 'r')
    final_data += f.read()
    f.close()

output_file_path = os.path.join(folder, final_inference)
write_output = open(output_file_path, 'w')
write_output.write(final_data)
write_output.close()
