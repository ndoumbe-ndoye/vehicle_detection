# Vehicle Counting Robustness Experiment

## Goal
Test how the detection/tracking/counting pipeline performs under different real-world conditions, and see whether a simple improvement strategy makes it more reliable.


## Known Failure Modes (found so far)
- **Misclassification at distance/small scale**: same physical car detected as "car" / "boat" / "train" at low confidence when far from camera — likely due to limited pixel detail.
- **Overlapping duplicate boxes**: a single small/distant car sometimes produces multiple overlapping low-confidence boxes, risking double-counting.
- **Jitter near the line**: a car sitting close to the line for multiple frames could flip sides due to pixel-level noise — fixed with a buffer zone.



### Table 1: Baseline Runs (no condition variable, threshold = 0.5)

Confidence threshold: **0.5**

| Clip name | Condition (clear/shadow/queued/occlusion/dense/etc.) | Length (s) | Manual count | Automated count | Error (manual − automated) | Notes / observations |
|---|---|---|---|---|---|---|
| Video 1 | Sunny, clear video quality, no occlusion | 30s | 25 | 20 | 5 | ID 9 not counted because its confidence score dropped to 0.31. One car was missed and not detected. ID 24 (bus) was only detected after it had already crossed the counting line. One older car was missed and not detected. ID 23 was missed because its confidence score dropped to 0.40. |
| Video 2 | Mostly clear, light fog, minimal occlusion (one instance) | 1:02 | 11 | 5 | 6 | ID 3's confidence score dropped to 0.47. One car was not detected. ID 7 and ID 8 were occluded by a truck. ID 16's confidence score dropped to 0.3. ID 13 was not detected despite having a confidence score of 0.56. At around 30s, a truck occluded two vehicles, and they were not counted. There were also two misclassifications: the road markings were identified as "bird" with a confidence score of 0.10, and the video itself was misclassified as "tv" with a confidence score of 0.10. |
| Video 3 | Dark, minimal lighting | 1:02 | 9 | 6 | 3 | A van and a truck were missed. ID 9 and ID 11 were detected only after crossing the counting line. ID 14 was also detected only after crossing the counting line. There was a misclassification of a railroad as a "train" with a confidence score above 0.80. |
| Video 4 | Good conditions, clear video quality, no occlusion | 25s | 21 | 20 | 1 | Only one vehicle was missed, a motorcycle. Overall performance was very good. |
| Video 5 | Dark, no street lighting, dense/queued traffic near the counting line | 23s | 30 | 43 | −13 (overcounted) | Vehicles clustered and overlapped right at the counting line, causing rapid, implausible count jumps (14 → 21 → 23 → 31 within about 2 seconds of video time).Many motorcyclists were not detected, and the ones that were detected were misclassified as "person." There was heavy misclassification of vehicle types overall, likely because the footage is not from the US and vehicle types/shapes differ ( most auto-rickshaws were missed entirely). |

### Table 2: Condition / Improvement: Using Fine-tuned model



| Clip name | Condition tested | Variable changed | Value before | Value after | Manual count | Automated count (before) | Automated count (after) | Notes / did it help? |
|---|---|---|---|---|---|---|---|---|
| Video 1 | Clear video quality, no occlusion | Model (baseline vs. fine-tuned) | YOLOv8n pretrained | Fine-tuned YOLOv8n | 25 | 20 | 8 | Count sat at 6 for most of the clip, then jumped to 8 right at the very end. Looked like the model kept re-detecting the same car(s) near the line as new objects instead of recognizing them as one continuous track, which pushed the count up without any real new crossings happening. |
| Video 2 | Mostly clear, light fog, minimal occlusion (one instance) | Model (baseline vs. fine-tuned) | YOLOv8n pretrained | Fine-tuned YOLOv8n | 11 | 5 | 4 | Alot of low confindenince score and late detections after the crossed line |
| Video 3 | Dark, minimal lighting | Model (baseline vs. fine-tuned) | YOLOv8n pretrained | Fine-tuned YOLOv8n | 9 | 6 | 3 |Low confidence score but most of thr vehichles were detected. |
| Video 4 | Good conditions, clear video quality, no occlusion | Model (baseline vs. fine-tuned) | YOLOv8n pretrained | Fine-tuned YOLOv8n | 21 | 20 | 2 |The motorcyle in this videoe was detected unlike with the pretrained model it wasnt, Overall low confident score bus the classifications here are spot on. Alot of cars were not detected. |
| Video 5 | Dark, dense/queued traffic, no street lighting | Model (baseline vs. fine-tuned) | YOLOv8n pretrained | Fine-tuned YOLOv8n | 30 | 43 | 3 | It was able to detect the car better but the classiication scoree were too low and it was able to detect 4 out 6 motorcyles. |