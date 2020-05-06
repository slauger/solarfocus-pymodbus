# Solarfocus Modbus TCP Examples

This repo contains some examples for querying the Solarfocus Modbus TCP interface via pymodbus.

The snippets were tested against a Solarfocus Octoplus heater with the EcoManager-Touch display.

## Read data

```
-bash$ python3 client.py 
## Outside temperature (address 2408)
ReadRegisterResponse (1)
[84]
The current outside temperature is 8.4 degrees Celsius

## Boiler temperature (address 2400)
ReadRegisterResponse (1)
[576]
The current boiler temperature is 57.6 degrees Celsius

## Boiler status (address 2401)
ReadRegisterResponse (1)
[0]
Current status is 0_Bereitschaft
```
