from pico_ice_spi import *
import binascii

# Open the port given as argument
spi = PicoIceSpi(sys.argv[1])

# Query the SRAM ID
spi.command(spi.USE_FPGA)
spi.write(b'\x01')
#                1   2   3   4	 1   2   3   4   1   2   3   4   
spi.write(b'\x06\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b')
spi.write(b'\x07')
id = spi.read(12)
print('FPGA_SPI_HW: ' + str(binascii.b2a_hex(id, ' ')))
spi.done()
