# VPEX
Vpu Pytorch EXtension

# Install Pytorch
Pytorch >= 2.4 required. 
Cpu version could be downloaded from [offical site](https://pytorch.org/).
```
pip3 install torch --index-url https://download.pytorch.org/whl/cpu
```

# Dependencies
- Python 3.8 or later.
- GCC 9.4.0 or newer is required.
- CMake 3.18 or later.
```
pip3 install cmake
``` 
- Optional: Ninja build tool
```
pip3 install ninja
```

# Build
```
cd vpex
mkdir build
cd build
export TORCH_INSTALL_PATH=$(python -c "import os;import torch;print(os.path.dirname(os.path.realpath(torch.__file__)))")
cmake -G Ninja -DCMAKE_PREFIX_PATH=${TORCH_INSTALL_PATH}/share/cmake ..
ninja
```

# Test
```
cd vpex
export PYTHONPATH=$PWD/python
python test/test.py
```

# Reference
- [Pytorch open registration example](https://github.com/bdhirsh/pytorch_open_registration_example)
- [OpenCL backend](https://github.com/artyom-beilis/pytorch_dlprim)
- [Ascend Npu](https://github.com/Ascend/pytorch)
- [Intel Extension for Pytorch](https://github.com/intel/intel-extension-for-pytorch)
