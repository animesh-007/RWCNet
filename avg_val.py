import json
import numpy as np
with open("/home/mvision/working_dir/RWCNet/ab_ctct_val_v1/metrics.json", 'r') as f:
    metrics = json.load(f)

dice_scores = [1-v["metrics"]["dice"] for v in  metrics.values()]
print(np.mean(dice_scores)) # 0.8048
