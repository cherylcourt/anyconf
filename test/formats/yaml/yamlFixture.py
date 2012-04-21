from testHelpers import usingPython3OrLater

if usingPython3OrLater():
  from io import StringIO
else:
  from StringIO import StringIO

import anyconf

class YamlFixture(object):
  def setup_method(self, method):
    self.configLoader = anyconf.ConfigLoader()

  def loadConfigWithContent(self, content):
    fileObj = StringIO(content)
    return self.configLoader.load(fileObj, anyconf.FORMAT_YAML)


