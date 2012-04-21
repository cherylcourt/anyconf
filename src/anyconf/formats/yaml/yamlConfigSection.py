from ...configSection import ConfigSection

class YamlConfigSection(ConfigSection):

  def __init__(self, entry):
    super(YamlConfigSection, self).__init__()
    self.entry = entry

  def getChildren(self):
    if self._hasChildren(self.entry):
      return self.entry

  def _getChild(self, name):
    try:
      return self._yamlEntryToConfigEntry(self.entry[name])
    except KeyError:
      return None

  def _yamlEntryToConfigEntry(self, entry):
    if self._hasChildren(entry):
      return YamlConfigSection(entry)
    elif (type(entry) is list) and (type(entry[0]) is dict):
      convertedList = []
      for entryItem in entry:
        convertedList.append(self._yamlEntryToConfigEntry(entryItem))
      return convertedList
    else:
      return self._getValue(entry)

  def _hasChildren(self, entry):
    return type(entry) is dict

  def _getValue(self, entry):
    if entry is None:
      return True
    else:
      return entry

