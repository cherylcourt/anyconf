import string, random, sys

def uniqStr():
  return random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(20))

def usingPython3OrLater():
  return sys.version_info[0] >= 3


