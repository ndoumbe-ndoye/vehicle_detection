
all_scores = []
all_frames = {}
frames_average = {}
with open("detections/detection.txt", "r") as file:
    next(file)
    for line in file:
        parts = line.split(",")
        conf = float(parts[2])
        all_scores.append({
        "filename": parts[0],
        "class": parts[1],
        "confidence": conf,
        "box": parts[3]
    })
        if parts[0] in all_frames:
            all_frames[parts[0]].append(conf)
        else:
            all_frames[parts[0]] = [conf]

for frames in all_frames:
    frames_average[frames] = sum(all_frames[frames]) / len(all_frames[frames])

sorted_list =  sorted(frames_average.items(), key=lambda x: x[1], reverse=True)

highest_five = sorted_list[0:5]
lowest_five = sorted_list[-5:]

print(f"The top 5 highest confidence scores")
for score in highest_five:
    print("filenamee:", score[0], "Class type:", score[1])

print(f"The top 5 lowest confidence scores")
for score in lowest_five:
        print("filenamee:", score[0], "Class type:", score[1])