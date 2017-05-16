Title: How to program a uC preloaded with Arduino-bootloader from AVRStudio
Date: 2017-05-16 17:00

To-do: Explain the different ways of programming a microcontroller, its memory zones, bootloader zone, fuses, etc.

These are the steps to program a microcontroller (e.g. Atmega328p, aka *Arduino Pro Mini*),
preloaded with an **Arduino-compatible bootloader** directly...

## From AVR Studio

* Install avrdude from [the WinAVR project](https://sourceforge.net/projects/winavr/files/latest/download), or find its path inside an installation of the ArduinoIDE.
* Open the Atmel Studio IDE.
* Go to the `Tools` menu and choose `External Tools`.
* Add a new one named `avrdude`, with its path pointing to the `avrdude.exe` file you found in the first step above.
* In `Arguments`, write the following (for Arduino Pro Mini, Atmega328p), obviously **replacing** the path to `avrdude.conf`, the **serial port** name with your own actual values. Alternatively, replace the quoted string between `:w:` and `:i` with the full, absolute path of the final `.hex` file produced by your project compilation.

        -C "C:\avrdude\avrdude.conf" -p atmega328p -c arduino -P COM9 -b 57600 -U flash:w:"$(ProjectDir)Debug\$(ItemFileName).hex":i


## From a Linux terminal

* Install avrdude:

          sudo apt install avrdude

* Take the compiled program in `.hex` format and program it with:

          avrdude -p atmega328p -c arduino -P /dev/ttyUSB0 -b 57600 -U flash:w:"YOURPROGRAM.hex":i
