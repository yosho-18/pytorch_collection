import torch
x1 = torch.tensor([[1, 1], [1, 1.]])  # 2×2
x2 = torch.tensor([[2, 2, 3], [2, 4, 2.]])  # 2×3


#x1 = torch.tensor([[1, 2], [3, 4]])  # 2×2
#x2 = torch.tensor([[10, 20, 30], [40, 50, 60.]])  # 2×3


# dim=1に対して結合することで2×5のTensorを作る
print(torch.cat([x1, x2], dim=1))
# HWCをCHWに変換
# 64×32×3のデータが100個
#hwc_img_data = torch.rand(100, 64, 32, 3); print(hwc_img_data)
#chw_img_data = hwc_img_data.transpose(1, 2).transpose(1, 3); print(hwc_img_data)


