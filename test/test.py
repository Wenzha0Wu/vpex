import torch
import torch_vpu

print(torch.vpu.device_count())
print(torch_vpu.device(0))

x = torch.ones(4, 4, device='vpu')
y = torch.ones(4, 4, device=torch_vpu.device(0))
z = x + y

print(z.cpu())
print(x.cpu())

