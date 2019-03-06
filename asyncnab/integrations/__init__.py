import json
from copy import copy
import asyncio
import requests


class Integrations(object):

    def __init__(self, bank):
        self.bank = bank
