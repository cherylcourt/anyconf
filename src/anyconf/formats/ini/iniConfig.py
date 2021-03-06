from ...formats import FORMAT_INI
from ...config import Config
from .iniConfigSection import IniConfigSection

import sys
if sys.version_info[0] >= 3:
  from configparser import ConfigParser
else:
  from ConfigParser import ConfigParser

class IniConfig(Config):
  def __init__(self):
    super(IniConfig, self).__init__(FORMAT_INI)

  def loadFromFile(self, inputFile):
    self.parser = ConfigParser()
    self.parser.readfp(inputFile)

  def getChildren(self):
    out = {}
    for section in self.parser.sections():
      out[section] = IniConfigSection(section, self.parser)
    return out

  def _getChild(self, name):
    if self.parser.has_section(name):
      return IniConfigSection(name, self.parser)
    return None

