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
import pandas as pd
import numpy as np

website = "https://api.nasa.gov/DONKI/CME?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=iZfqQhESERl9LDQep7Wh3Lgubr3USaX9MqXhjCi3"

var xhr = new XMLHttpRequest();
xhr.open('GET', website, true);
xhr.onreadystatechange = function() {
  if (xhr.readyState == 4) {
    console.log(xhr.responseText);
  }
}
xhr.send();

print(website);