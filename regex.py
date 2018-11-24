import re
batmanReg = re.compile(r'Bat(wo)?man')
batmanSearch = batmanReg.search("the adventure of Batman and Batwoman")
print(batmanSearch.group(0))