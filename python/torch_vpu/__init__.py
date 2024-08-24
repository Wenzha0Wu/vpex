import torch
import torch_vpu._C.libvpex as libvpex


def device(device_idx=0):
    return libvpex.custom_device(device_idx)


class _VpuModule:

    @staticmethod
    def device_count():
        return libvpex.getDeviceCount()

    @staticmethod
    def is_available():
        return True

    @staticmethod
    def is_autocast_enabled():
        return True

    @staticmethod
    def get_autocast_dtype():
        return torch.float16

    @staticmethod
    def set_autocast_enabled(enable):
        pass

    @staticmethod
    def set_autocast_dtype(dtype):
        pass

    @staticmethod
    def get_amp_supported_dtype():
        return [torch.float16]


torch.utils.rename_privateuse1_backend('vpu')
torch._register_device_module("vpu", _VpuModule)
