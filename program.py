import requests
import json
import sys
import os
import time
import datetime
import logging
import logging.handlers
import argparse
import configparser
import re
import csv
import io

#website = "https://api.nasa.gov/DONKI/CME?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=iZfqQhESERl9LDQep7Wh3Lgubr3USaX9MqXhjCi3"

x = requests.get("https://api.nasa.gov/DONKI/CME?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=iZfqQhESERl9LDQep7Wh3Lgubr3USaX9MqXhjCi3")
print(x.status_code)

print(x); #We get a good response!