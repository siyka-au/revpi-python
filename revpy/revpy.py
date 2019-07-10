import struct, fcntl, os

__all__ = [ 'RevPy' ]

# Add the rest of the functions from
# https://github.com/RevolutionPi/piControl/blob/master/piTest/piControlIf.c

# Module Id
# 0x0001 - 0x3000      KUNBUS Modules (e.g. DIO, Gateways, ...)
# 0x3001 - 0x7000      not used
# 0x6001 - 0x7000      KUNBUS Software Adapters
# 0x7001 - 0x8000      User defined Software Adapters
# 0x8001 - 0xb000      KUNBUS Modules configured but not connected
# 0xb001 - 0xffff      not used
PICONTROL_SW_OFFSET= 0x6001
PICONTROL_SW_MODBUS_TCP_SLAVE = 0x6001
PICONTROL_SW_MODBUS_RTU_SLAVE = 0x6002
PICONTROL_SW_MODBUS_TCP_MASTER = 0x6003
PICONTROL_SW_MODBUS_RTU_MASTER = 0x6004
PICONTROL_SW_PROFINET_CONTROLLER = 0x6005
PICONTROL_SW_PROFINET_DEVICE = 0x6006
PICONTROL_SW_REVPI_SEVEN = 0x6007
PICONTROL_SW_REVPI_CLOUD = 0x6008
PICONTROL_NOT_CONNECTED = 0x8000
PICONTROL_NOT_CONNECTED_MASK = 0x7fff

KB_CMD1 = 19210
KB_CMD2 = 19211
KB_RESET = 19212
KB_GET_DEVICE_INFO_LIST = 19213
KB_GET_DEVICE_INFO = 19214
KB_GET_VALUE = 19215
KB_SET_VALUE = 19216
KB_FIND_VARIABLE = 19217
KB_SET_EXPORTED_OUTPUTS = 19218
KB_UPDATE_DEVICE_FIRMWARE = 19219
KB_DIO_RESET_COUNTER = 19220
KB_GET_LAST_MESSAGE = 19221
KB_STOP_IO = 19222
KB_CONFIG_STOP = 19223
KB_CONFIG_SEND = 19224
KB_CONFIG_START = 19225
KB_SET_OUTPUT_WATCHDOG = 19226
KB_WAIT_FOR_EVENT = 19250
KB_EVENT_RESET = 1
KB_INTERN_SET_SERIAL_NUM = 19300
KB_INTERN_IO_MSG = 19301


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
    
    def writeBit(self, offset: int, bit: int, value: bool):
        pSpiValue = struct.pack('HBB', offset, bit, 1 if value else 0)
        fcntl.ioctl(PiControlHandle_g, KB_SET_VALUE, pSpiValue)

    def readBit(self, offset: int, bit: int) -> bool:
        int piControlGetBitValue(SPIValue * pSpiValue) {
            piControlOpen();

            if (PiControlHandle_g < 0)
                return -ENODEV;

            pSpiValue->i16uAddress += pSpiValue->i8uBit / 8;
            pSpiValue->i8uBit %= 8;

            if (ioctl(PiControlHandle_g, KB_GET_VALUE, pSpiValue) < 0)
                return -errno;

            return 0;
        }

    def reset(self):
        ioctl(PiControlHandle_g, KB_RESET, NULL)

    def close(self):
        os.close(self.fd)
