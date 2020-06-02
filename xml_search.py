import xml.etree.ElementTree as et


root = et.parse("a.txt")
result = ''

print(root.find('./bookstore'))

# How to make decisions based on attributes even in 2.6
for e in root.findall('.//title[@lang=\'en\']'):
    try:
        print(e)
        if "en" in e:
            print(e)
    except Exception :
        pass
