from serial import Serial, EIGHTBITS, PARITY_ODD, STOPBITS_ONE

s = Serial("/dev/ttyUSB0",
                    baudrate=1200,
                    bytesize=EIGHTBITS,
                    parity=PARITY_ODD,
                    stopbits=STOPBITS_ONE,
                    timeout=2,rtscts=True)
# s.write(bytes.fromhex("00000000000000000000000000000000"))
# s.write(bytes.fromhex("05000000"))

# response = s.read(512)
# #pass#print(response.hex())
s.write(bytes.fromhex("ffffffffff0280000082"))
response = s.read(512)
#pass#print(response.hex())

# s.write(bytes.fromhex("ffffffffff0280000082"))
# response = s.read(512)
# #pass#print(response.hex())

# s.write(bytes.fromhex("ffffffffff8293200000000f003e"))
# response = s.read(128)

# #pass#print(response.hex())
