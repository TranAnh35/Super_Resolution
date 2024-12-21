# import thư viện cần thiết
import torch
import torch.nn as nn

class SFB(nn.Module):
    def __init__(self, embed_dim):
        super(SFB, self).__init__()
        # Định nghĩa các phần tử trong khối tại đây
        # T đề nghĩ hãy viết thành 2 class con là nhánh trái và nhánh phải để cho clean
        pass
        
    def __call__(self, x):
        # Sẽ viết hương mà dữ liệu được sử lý tại đây
        """ Ví dụ
        
        x_trai = nhanh_phai(x)
        x_phai = nhanh_trai(x)
        output = cat(x_trai, x_phai)
        output = conv(output)
        return output
        """
        pass
    

class MLP(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
    
    def __call__(self, *args, **kwds):
        pass
    
class WindowAttention(nn.Module):
    # Window based  multi-head self attention (W-MSA)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
    
    def __call__(self, *args, **kwds):
        pass
    
class STL(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
    
    def __call__(self, *args, **kwds):
        pass
    
class RSTB(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
    
    def __call__(self, *args, **kwds):
        pass