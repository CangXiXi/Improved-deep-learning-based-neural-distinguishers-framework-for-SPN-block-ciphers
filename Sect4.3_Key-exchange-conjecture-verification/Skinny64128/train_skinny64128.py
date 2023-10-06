from train_nets import train_distinguisher
from skinny64128 import Skinny64128

skinny = Skinny64128(n_rounds=7)
train_distinguisher(
    skinny, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0], n_epochs=30, case=1, lr_high=0.0011, lr_low=0.000045,
    kernel_size=3, reg_param=0.000000043
)