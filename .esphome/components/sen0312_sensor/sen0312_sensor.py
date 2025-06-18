import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, sensor
from esphome.const import CONF_ID, UNIT_MILLIMETER, ICON_RULER

sen0312_ns = cg.esphome_ns.namespace("sen0312")

PollingComponent = cg.global_ns.class_("PollingComponent", cg.Component)
Sensor = cg.global_ns.class_("Sensor", cg.Component)

SEN0312Sensor = sen0312_ns.class_("SEN0312Sensor", PollingComponent, Sensor)

CONFIG_SCHEMA = (
    sensor.sensor_schema(  # Safe again
        unit_of_measurement=UNIT_MILLIMETER,
        accuracy_decimals=0,
        icon=ICON_RULER
    )
    .extend({
        cv.GenerateID(): cv.declare_id(SEN0312Sensor),
    })
    .extend(cv.polling_component_schema("1s"))
    .extend(uart.UART_DEVICE_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config[uart.CONF_UART_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    await uart.register_uart_device(var, config)

