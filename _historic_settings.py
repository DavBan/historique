import yaml
import json
from enum import StrEnum

import os
import sys
import getopt

class ConfigsEnum(StrEnum):
    HISTORY_SIZE = "history-size"
    LOGGING_FILE = "logfile"

try:
    opts, args = getopt.getopt(sys.argv[1:], "c:f:", ["config-file=", "format="])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

if len(args)>1:
    raise getopt.GetoptError("Too many argument given, arguments :" + args[1:] + "were not expected")

optdict = dict(opts)
mutually_exclusive = [
        ["-c", "--config-file"],
        ["-f", "--format"]
]

for exclusive in mutually_exclusive:
    if list((x in exclusive for x in optdict)).count(True) > 1:
        raise getopt.GetoptError("Only one config file has to be specified.")
    
if len([config for config in optdict if config in ["-c", "--config-file"]]) == 1 and len(args) == 1:
    raise getopt.GetoptError("Only one config file has to be specified.")

config_file = args[0] if len(args)==1 else os.getcwd() + "config.yml"

config_opt = [optdict[config] for config in optdict if config in ["-c", "--config-file"]]
if len(config_opt) == 1:
    config_file = config_opt [0]

format_opt = [optdict[fmt] for fmt in optdict if fmt in ["-f", "--format"]]

file_format = "YAML" if len(format_opt) == 0 else format_opt[0]


default_config = {
    ConfigsEnum.HISTORY_SIZE: -1,
    ConfigsEnum.LOGGING_FILE: ""
}
config = {}
parser = yaml.safe_load
parsererror = yaml.YAMLError
if file_format == "YAML":
    parser = yaml.safe_load
    parsererror = yaml.YAMLError
elif file_format == "JSON":
    parser = json.loads
    parsererror = ValueError
if os.path.isfile(config_file):
    with open(config_file) as formatted_stream:
        try:
            loaded_config = parser(formatted_stream)
            config = loaded_config
        except parsererror as exc:
            print(exc)
for conf in default_config:
    config[conf] = default_config if conf not in config else config[conf]




