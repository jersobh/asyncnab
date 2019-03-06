import json
from copy import copy
import asyncio
import requests


class Asyncnab(object):

    def __init__(self, environment):
        self.environment = environment
