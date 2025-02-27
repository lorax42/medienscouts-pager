# Pager

* ESP32
* LiPo battery

## Sequence Plan

* default state: sleeping
* periodically wake up
* connect to wifi
* poll web API for message
* display message if available
* turn off wifi
* go to sleep
