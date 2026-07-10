import matplotlib.pyplot as plt
import mplcursors
import numpy as np
import os

# represent each test video on the x-axis
x = ["Video 1", "Video 2", "Video 3", "Video 4", "Video 5"]
position = np.arange(len(x))
width_bar = 0.25

# manual (ground truth) counts
manual = [25, 11, 9, 21, 30]
# pretrained YOLOv8n model counts
pretrained = [20, 5, 6, 20, 43]
# fine-tuned model counts
fine_tuned = [8, 4, 3, 2, 3]

bars1 = plt.bar(position - width_bar, manual, width_bar, label="Manual Count")
bars2 = plt.bar(position, pretrained, width_bar, label="Pretrained Model")
bars3 = plt.bar(position + width_bar, fine_tuned, width_bar, label="Fine-Tuned Model")

plt.xlabel("Test Videos")
plt.ylabel("Count of Detected Vehicles")
plt.title("Manual vs Automated Vehicle Counts")
plt.yticks(range(0, 50, 5))
plt.xticks(position, x)
plt.legend()

cursor = mplcursors.cursor([bars1, bars2, bars3], hover=True)
# artist is which bar you're hovering over (manual, pretrained, or fine-tuned)
# target is the (x, y) point on that bar; target[1] is the count value
cursor.connect("add", lambda sel: sel.annotation.set_text(f"{sel.artist.get_label()}: {sel.target[1]:.0f}"))

output_folder = "counts_experiment"
os.makedirs(output_folder, exist_ok=True)
file_path = os.path.join(output_folder, "experiment_results.png")
plt.savefig(file_path)
plt.show()