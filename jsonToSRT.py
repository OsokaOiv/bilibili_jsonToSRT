import json
import math
import os

file = ''  # This variable is used to save data
i = 1
for doc in os.listdir():  # Traverse all files in the current folder
    if doc[-4:] == 'json':  # If it is a json file, process it
        name = doc[:-5]  # Extract the file name
        # Modify the file location here, add utf-8 to avoid errors when processing Chinese
        with open(doc, encoding='utf-8') as f:
            datas = json.load(f)  # Load file data
            f.close()
        for data in datas['body']:
            start = data['from']  # Get start time
            stop = data['to']  # Get end time
            content = data['content']  # Get subtitle content
            file += '{}\n'.format(i)  # Add serial number
            hour = math.floor(start) // 3600
            minute = (math.floor(start) - hour * 3600) // 60
            sec = math.floor(start) - hour * 3600 - minute * 60
            mil_sec = int((start - hour * 3600 - minute * 60 - sec)*1000)
            file += str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(sec).zfill(2) + ',' + str(
                mil_sec).zfill(2)  # Fill the number with 0 and write it according to the format
            file += ' --> '
            hour = math.floor(stop) // 3600
            minute = (math.floor(stop) - hour * 3600) // 60
            sec = math.floor(stop) - hour * 3600 - minute * 60
            mil_sec = abs(int((stop - hour * 3600 - minute * 60 - sec)*1000))
            file += str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(sec).zfill(2) + ',' + str(
                mil_sec).zfill(2)
            file += '\n' + content + '\n\n'  # Add subtitle text
            i += 1
        with open('./{}.srt'.format(name), 'w', encoding='utf-8') as f:
            f.write(file)  # Write data to file
            f.close()
        file = ''
        i = 1

