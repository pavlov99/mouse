try:
    from lxml import etree
except ImportError:
    try:
        import xml.etree.cElementTree as etree
    except ImportError:
        import xml.etree.ElementTree as etree

from collections import namedtuple


class CheddargetterParser(object):

    """ Cheddargetter xml response parser.

    Parser generates objects from Cheddargetter xml, objects are generated
    on the fly. Class for object has fields defined based on xml.

    """

    @classmethod
    def parse(cls, root):
        children = root.getchildren()
        if not children:
            return (root.tag, root.text)
        else:
            items = []
            for child in children:
                item = dict(
                    [cls.parse(field) for field in child.getchildren()] +
                    child.items()
                )
                class_ = namedtuple(child.tag.capitalize(), item.keys())
                items.append(class_(**item))

            return (root.tag, items)


root = etree.fromstring(open("mouse/tests/xml/plans.xml").read())
print(etree.tostring(root))
plans = CheddargetterParser.parse(root)[1]
