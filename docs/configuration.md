# Configuration Guide

## Required Secrets

Ensure the following are defined in your `secrets.yaml`:

```yaml
wifi_ssid: "YourWiFiSSID"
wifi_password: "YourWiFiPassword"
ota_password: "YourOTAPassword"
api_encryption_key: "A_long_secure_generated_key"
```

## Flashing Instructions

1. Connect the ESP32-C3 to your PC via USB.
2. Run `esphome run sump.yaml` to compile and flash.
3. After flashing, device will reboot and attempt to join Wi-Fi.

## Accessing the Web UI

Once connected to your network, visit the IP address assigned to the device to see the live values in the built-in ESPHome web server.
