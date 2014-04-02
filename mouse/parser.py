try:
    from lxml import etree
except ImportError:
    try:
        import xml.etree.cElementTree as etree
    except ImportError:
        import xml.etree.ElementTree as etree

from decimal import Decimal
import dateutil.parser


datetime_type = lambda x: x if x is None else dateutil.parser.parse(x)


class CheddargetterParser(object):

    """ Cheddargetter xml response parser.

    Parser generates objects from Cheddargetter xml, objects are generated
    on the fly. Class for object has fields defined based on xml.

    """

    CONVERTER = {
        "isActive": bool,
        "isFree": bool,
        "isPeriodic": bool,
        "isVatExempt": bool,
        "trialDays": int,
        "billingFrequencyQuantity": int,
        "setupChargeAmount": Decimal,
        "recurringChargeAmount": Decimal,
        "quantityIncluded": Decimal,
        "overageAmount": Decimal,
        "quantity": Decimal,
        "eachAmount": Decimal,
        "createdDatetime": datetime_type,
        "firstContactDatetime": datetime_type,
        "modifiedDatetime": datetime_type,
        "ccExpirationDate": datetime_type,
        "canceledDatetime": datetime_type,
        "billingDatetime": datetime_type,
    }

    @classmethod
    def parse_to_class(cls, element):
        item = dict(
            [cls.parse(field) for field in element.getchildren()] +
            element.items()
        )

        if element.tag == "error":
            from .exceptions import CheddargetterException
            item.update(message=element.text)
            return CheddargetterException.instantiate(**item)
        else:
            from .models import Factory
            return Factory.instantiate(element.tag.capitalize(), **item)

    @classmethod
    def parse(cls, root):
        children = root.getchildren()
        if not children:
            if root.tag == "error":
                return (root.tag, cls.parse_to_class(root))

            value = root.text
            if value is not None:
                convert = cls.CONVERTER.get(root.tag, str)
                if convert == str:
                    value = value.encode("utf8")
                value = convert(value)

            return (root.tag, value)
        else:
            if root.tag == "gatewayAccount":
                return (root.tag, cls.parse_to_class(root))
            else:
                items = [cls.parse_to_class(child) for child in children]
                return (root.tag, items)

    @classmethod
    def parse_xml(cls, xml):
        return cls.parse(etree.fromstring(xml))
