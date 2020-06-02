with open('regular.txt', 'r') as f:
    data = f.readlines()
    f.close()

processed_output = []

for each_line in data:
    if not (each_line.startswith('NEW MIN') or each_line.startswith('mAP')):
        split_data = each_line.split('=')
        processed_output.append(split_data[1].replace('AP', '').strip() + ',' + split_data[0].strip())

with open('regular_output.txt', 'w') as f:
    f.write('class_name,mAP score\n')
    f.write("\n".join(processed_output))
    f.close()
