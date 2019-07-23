import torch
x = torch.empty(5, 3)         # 0埋め
print(x)
x = x.new_ones(3, 2, dtype=torch.double)   # 既存のtensorの型変換&1埋め
print(x)
x = torch.rand(4, 2)                       # 乱数
print(x)
x = torch.randn_like(x, dtype=torch.float) # 既存のtensorを乱数で埋める
print(x)
x = torch.tensor([5.5, 3])                 # データから直接構成
print(x)
x.size()                                   # サイズ取得

# Tensor用にdeviceを定義
device = torch.device('cuda:' + str(args.gpu)
                      if torch.cuda.is_available() else 'cpu')

orig_trajs = torch.from_numpy(orig_trajs).float().to(device)  # Creates a Tensor from a numpy.ndarray.