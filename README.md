# logstyle

# Getting started

Logstyle was developed for simplified usage like in below examples:

* Create your own CustomLog instance
```
custom_logger = CustomLog("MyLogger")
```
* Now you can try it using different  styles and colors like below:
  * Box style logs:
  ```
  custom_logger.box_log("This is a box log example.", CustomLog.COLOR_GREEN)
  ```
  * Title style logs:
  ```
  custom_logger.title_log("Title Log", "This is a title log example.", CustomLog.COLOR_BLUE)
  ```
  * JSON style logs:
  ```
   custom_logger.json_log("JSON Log", "This is a JSON log example.", {"key": "value"}, CustomLog.COLOR_AMBER)
  ```
  * YAML style logs:
  ```
  custom_logger.yaml_log("YAML Log", "This is a YAML log example.", {"key": "value"}, CustomLog.COLOR_RED)
  ```