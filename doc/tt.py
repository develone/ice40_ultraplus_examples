from pico_ice_spi import *
import binascii

# Open the port given as argument
spi = PicoIceSpi(sys.argv[1])

# Query the SRAM ID
spi.command(spi.USE_FPGA)
spi.write(b'\x01')
#                1   2   3   4	 
#spi.write(b'\x04\x00\x00\x00\xff')
spi.write(b'\x04\x0f')
#spi.done()
