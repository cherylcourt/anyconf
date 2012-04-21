from __future__ import with_statement

import pytest

from anyconf.configFactory import ConfigFactory
from anyconf.formats import FORMAT_INI, FORMAT_YAML, FORMAT_XML
from anyconf.formats.ini.iniConfig import IniConfig
from anyconf.formats.xml.xmlConfig import XmlConfig
from anyconf.formats.yaml.yamlConfig import YamlConfig
from anyconf.unknownConfigFormatError import UnknownConfigFormatError

class WhenGettingConfigFromConfigFactory:

  def testThatConfigFactoryReturnsIniConfigForIniFormat(self):
    obj = ConfigFactory().getConfig(FORMAT_INI)
    assert isinstance(obj, IniConfig)

  def testThatConfigFactoryReturnsIniConfigForIniFormat(self):
    obj = ConfigFactory().getConfig(FORMAT_XML)
    assert isinstance(obj, XmlConfig)

  def testThatConfigFactoryReturnsYamlConfigForYamlFormat(self):
    obj = ConfigFactory().getConfig(FORMAT_YAML)
    assert isinstance(obj, YamlConfig)

  def testThatAnUnknownFormatThrowsUnknownConfigFormatError(self):
    FORMAT_NOTHING = 0
    with pytest.raises(UnknownConfigFormatError):
      ConfigFactory().getConfig(FORMAT_NOTHING)

