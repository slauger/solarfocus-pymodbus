#!/usr/bin/env python3

from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('10.0.0.230', 502)

# Außentemperatur
print("## Outside temperature (address 2408)")
result = client.read_input_registers(2408, unit=0x04)
print(result)
print(result.registers)
print("The current outside temperature is " + str(result.registers[0] / 10) + " degrees Celsius\n")

# Kesseltemperatur
print("## Boiler temperature (address 2400)")
result = client.read_input_registers(2400, unit=0x04)
print(result)
print(result.registers)
print("The current boiler temperature is " + str(result.registers[0] / 10) + " degrees Celsius\n")

# Statuszeile Kessel
print ("## Boiler status (address 2401)")
status_mapping = {
  0: "0_Bereitschaft",
  1: "1_Zuendphase",
  2: "2_Pelletsbetrieb"
  # ...
}

result = client.read_input_registers(2401, unit=0x04)
print(result)
print(result.registers)
status = result.registers[0]

if status in status_mapping:
  print("Current status is " + status_mapping[status])
else:
  print("Current status is unkown (" + str(code) + ")")

client.close()
