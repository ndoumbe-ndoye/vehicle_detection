import matplotlib.pyplot as plt
import mplcursors
import numpy as np
import os 

# represent the segments in the x-axis (every 6 second intervals)
x = [ "seg1", "seg2", "seg3", "seg4", "seg5", "seg6"]

position = np.arange(len(x))    
width_bar = 0.35

# count of detected vehicles in segment1 
mannual = [10, 22, 30, 39, 52, 58]
model = [12, 25, 33, 42, 55, 61]
# left side of the bar 
bars1 = plt.bar( position - width_bar/2, mannual, width_bar, label = "Mannual Count")
# right side of the bar
bars2 = plt.bar( position + width_bar/2,  model, width_bar, label = "Model Count")

plt.xlabel("Segments of Counting Video")
plt.ylabel("Count of detected vehicles")
plt.title("Count of objects detected in each segment")
plt.yticks(range(0,75,5))
plt.xticks(position, x)
plt.legend()
cursor = mplcursors.cursor([bars1, bars2], hover=True)
# artist is which bar your hovering over manual or model 
# # text is the text that will be displayed when hovering over the bar
# annotation is the text box that will be displayed when hovering over the bar 
cursor.connect("add", lambda sel: sel.annotation.set_text(f"{sel.artist.get_label()}: {sel.target[1]:.0f}"))
output_folder = "counts"
file_path = os.path.join(output_folder, "counts_visual.png")
plt.savefig(file_path)
plt.show()
