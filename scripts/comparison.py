import cv2
import numpy as np
import os

frames = {
    # SUCCESS CASES
    "frameV41040.jpg": "frames4",
    "frameV41020.jpg": "frames4",
    "frameV1840.jpg": "frames",
    "frameV20.jpg": "frames2",
    "frameV5360.jpg": "frames5",

    # FAILURE CASES
    "frameV5140.jpg": "frames5",
    "frameV3460.jpg": "frames3",
    "frameV5120.jpg": "frames5",
    "frameV6320.jpg": "frames6",
    "frameV660.jpg": "frames6"
}


for frame, folder in frames.items():

    original = cv2.imread(f"{folder}/{frame}")

    detected = cv2.imread(
        f"detections/{frame[:-4]}_detection.jpg"
    )
    comparison = np.hstack((original, detected))

    cv2.imwrite(
        f"figures/comparison_{frame}",
        comparison
    )

    print(f"Saved comparison_{frame}")