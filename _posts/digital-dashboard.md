---
image:
    path: https://github.com/Sneupi/digital-dashboard/blob/main/exampleproject.jpg?raw=true
---
# [digital-dashboard](https://github.com/Sneupi/digital-dashboard/blob/main)

Source code for ESP32 based CAN-bus powered dashboard.

Reprogrammable to interpret & display any CAN-bus containing vehicle's CAN data.

Originally developed for Wildcat Formula Racing (University of Arizona) Formula SAE race car. 

# Get Started

1. Install VS Code
2. Install PlatformIO extension for VS Code
3. Plug ESP32 and restart VS Code
4. Within PlatformIO extension "Clone Git Project"
5. Upload to ESP32 using PlatformIO sidebar

# Re-Configurability

Configured as-is for example project below.

1. Pinouts for CAN transceiver and pushbutton. Open `pinout.h` source files to do so.

2. Vehicle-specific CAN-bus interpretation, open CAN source files (`limits.h`, `TranslateCAN.h`) for config instructions. For help decoding your vehicle, see related tool [can-analyzer](https://github.com/Sneupi/can-analyzer).

3. Compatible with wide range of TFT displays. Read [TFT_eSPI library documentation](https://github.com/Bodmer/TFT_eSPI) and edit library files accordingly (`User_Setup.h` or `User_Setup_Select.h`).

# Example Project
Project for University of Arizona FSAE racecar. Interprets custom MoTeC M150 CAN bus protocol.

![(image of example project)](https://github.com/Sneupi/digital-dashboard/blob/main/exampleproject.jpg?raw=true)

### IMPORTANT
ESP32 module requires 5V power (VIN or Micro USB) but GPIO pins operate at 3.3V

### Parts List

[ESP32 Microcontroller](https://www.amazon.com/dp/B08D5ZD528)

[CAN Transceiver (SN65HVD230)](https://www.amazon.com/gp/product/B00KM6XMXO)

[TFT Display 5" (SSD1963)](https://www.amazon.com/s?k=ssd1963+5+inch) 

...And any pushbutton will work

### Pinout

Note: PB = Pushbutton

Note: TFT_DC may be labeled "RS" depending on the TFT

| NAME | ESP32 GPIO |
| --- | --- |
| PB | 5 |
| --- | --- |
| CAN_RX | 18 |
| CAN_TX | 19 |
| --- | --- |
| TFT_CS | 33 |
| TFT_DC | 15 |
| TFT_RST | 32 |
| --- | --- |
| TFT_WR | 4 |
| TFT_RD | 2 |
| --- | --- |
| TFT_D0 | 12 |
| TFT_D1 | 13 |
| TFT_D2 | 26 |
| TFT_D3 | 25 |
| TFT_D4 | 17 |
| TFT_D5 | 16 |
| TFT_D6 | 27 |
| TFT_D7 | 14 |

# Common Issue: ESP32 not detected as COM port

You may try installing [VCP drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads)
