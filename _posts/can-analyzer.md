# [can-analyzer](https://github.com/Sneupi/can-analyzer/blob/main)
Analyzer-Translator tool for decoding automotive CAN bus

Originally intended for decoding data, in creation of custom [digital dashboard](https://github.com/Sneupi/digital-dashboard) project.

# Notes
1. Read `TranslateCAN.h` for tuning the tool to decode your vehicle
2. Set CAN_RX & CAN_TX in the `.ino` according to your CAN transciever wiring

# Project Requirements
1. Hardware req: ESP32 with CAN Transciever
2. Software req: Terminal emulator (such as Tera Term) that supports ANSI escape codes

# Serial Commands
| cmd | desc |
| --- | --- |
| m | switch to live CAN map |
| t | switch to live CAN translations |
