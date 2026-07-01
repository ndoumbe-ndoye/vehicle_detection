# Detection Error Analysis Table

| Frame | Precision | Recall | Error Type | Description |
|-------|-----------|--------|------------|-------------|
| frameV1140.jpg | 0.64 | 1.00 | False detection | High number of people detected — inflated YOLO count with non-vehicle detections |
| frameV1760.jpg | 0.73 | 1.00 | False detection | Same issue as V1140 — people detections lowered precision |
| frameV20.jpg | 0.40 | 1.00 | False detection | Large number of people and traffic lights detected, significantly lowering precision |
| frameV3200.jpg | 1.00 | 0.43 | Missed vehicle | Cars far from camera took up too few pixels; headlights from front cars distorted vehicles behind them; motorcycle missed entirely |
| frameV3460.jpg | 1.00 | 0.50 | Missed vehicle | Similar to V3200 — distant cars missed; motorcycle missed; right-lane vehicles not detected |
| frameV5140.jpg | 1.00 | 0.89 | Missed vehicle | Blurry video quality made distant cars indistinguishable — not enough pixels for confident detection |
| frameV51120.jpg | 1.00 | 0.83 | Missed vehicle | Same blurry video issue — far away cars lacked visible features for detection |
| frameV6280.jpg | 1.00 | 0.87 | Wrong class | Highway signage misclassified as train; van misclassified as truck; one semi-truck correctly labeled, the other misclassified as bus |
| frameV6340.jpg | 1.00 | 1.00 | Wrong class | Highway signage misclassified as train; distant cars missed due to small pixel footprint |
| frameV6580.jpg | 1.00 | 0.94 | Wrong class | Highway signage misclassified as train; van misclassified as bus; highway lane marking falsely detected as a car |