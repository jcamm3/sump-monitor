# Sump Water Level Monitor

Monitors sump water levels using the JSN-SR04T ultrasonic sensor. Reports measurements in both centimeters and inches. Integrates with Home Assistant and includes a built-in web interface.

## Features

- JSN-SR04T ultrasonic distance sensing
- Readouts in cm and inches
- OTA updates + encrypted Home Assistant API
- Web interface with grouped sensor values
- Wi-Fi fallback hotspot for recovery

## Hardware

- ESP32-C3 (Seeed Studio XIAO)
- JSN-SR04T Waterproof Ultrasonic Sensor

## Wiring

| Sensor Pin | ESP32-C3 Pin |
|------------|--------------|
| VCC        | 5V           |
| GND        | GND          |
| TRIG       | GPIO1        |
| ECHO       | GPIO3        |

## Getting Started

1. Flash the ESP32-C3 using ESPHome.
2. Update `!secret` values in your secrets file.
3. Save folders under .esphome directory to your local HA esphome directory.
4. Power up and connect to the fallback AP if Wi-Fi fails.
5. Access the web interface at `http://<device-ip>`.

## License

MIT License
