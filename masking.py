import torch
conf_scores = torch.tensor([[.6,.6,.6,.5,.5,.5,.4,.4,.4]])
cl =0
conf_thresh = 0.5
c_mask = conf_scores[cl].gt(conf_thresh)
scores = conf_scores[cl][c_mask]
pass
