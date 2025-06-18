#include "esphome.h"

class SEN0312Sensor : public PollingComponent, public sensor::Sensor {
 public:
  SEN0312Sensor(UARTComponent *uart) : uart_(uart) {}

  void update() override {
    while (uart_->available()) {
      uint8_t b = uart_->read();
      buffer_.push_back(b);
    }

    while (buffer_.size() >= 9) {
      if (buffer_[0] == 0xFF && buffer_[1] == 0xFF && buffer_[8] == 0xFE) {
        uint16_t distance = (buffer_[2] << 8) | buffer_[3];
        publish_state(distance);
        buffer_.clear();
        return;
      } else {
        buffer_.erase(buffer_.begin());
      }
    }
  }

 protected:
  UARTComponent *uart_;
  std::vector<uint8_t> buffer_;
};
