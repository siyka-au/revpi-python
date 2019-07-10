import os

__all__ = [ 'RevPy' ]

class RevPy():
    def __init__(self):
        self.fd = os.open("/dev/piControl0", os.O_RDWR)
    
    def __checkOffset(self, offset: int):
        if (offset <= 0):
            raise ValueError('offset must be > 0')
        if (offset > 65535):
            raise ValueError('offset must be <= 65535')
    
    def __checkLength(self, length: int):
        if (length <= 0):
            raise ValueError('length must be > 0')
        if (length > 65535):
            raise ValueError('length must be <= 65535')

    def write(self, offset: int, data: bytes):
        self.__checkOffset(offset)
        self.__checkLength(len(data))
        os.lseek(self.fd, offset, os.SEEK_SET)
        os.write(self.fd, data)
    
    def read(self, offset: int, length: int) -> bytes:
        self.__checkOffset(offset)
        self.__checkLength(length)
        os.lseek(self.fd, offset, os.SEEK_SET)
        return os.read(self.fd, length)
    
    def close(self):
        os.close(self.fd)
