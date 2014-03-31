""" Settings are based on https://cheddargetter.com/developers"""
from .utils import FrozenDict, Singleton
from . import six


@six.add_metaclass(Singleton)
class CheddargetterSettings(object):
    pass


settings = CheddargetterSettings()

settings.USERNAME = ""
settings.PASSWORD = ""
settings.PRODUCT_CODE = "PYTHON_MOUSE_TESTING"
settings.BASE_URL = "https://mouse.chargevault.com"
settings.REQUEST_MAP = (
    FrozenDict(
        title="Get All Pricing Plans",
        doc="Get all pricing plan data from the product with " +
        "productCode={product_code}",
        path="/plans/get/productCode/{product_code}",
        request_method="GET",
    ),
    FrozenDict(
        title="Get a Single Pricing Plan",
        doc="Get the pricing plan data from the product with " +
        "productCode={product_code} for the pricing plan with " +
        "code={plan_code}",
        path="/plans/get/productCode/{product_code}/code/{plan_code}",
        request_method="GET",
    ),
    FrozenDict(
        title="Get All Customers",
        doc="Get all customer data from the product with " +
        "productCode={product_code}",
        path="/customers/get/productCode/{product_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Get a Single Customer By Code",
        doc="Get the customer data from the product with " +
        "productCode={product_code} for the customer with " +
        "code={customer_code}",
        path="/customers/get/productCode/{product_code}/code/{customer_code}",
        request_method="GET",
    ),
    FrozenDict(
        title="Get a Single Customer By Invoice Number",
        doc="Get the customer data from the product with " +
        "productCode={product_code} for the customer with "
        "invoiceNumber={invoice_number}",
        path="/customers/get/productCode/{product_code}/invoiceNumber/" +
        "{invoice_number}",
        request_method="GET",
    ),
    FrozenDict(
        title="Get a Single Customer By Id",
        doc="Get the customer data from the product with " +
        "productCode={product_code} for the customer with "
        "id={customer_id}",
        path="/customers/get/productCode/{product_code}/id/{customer_id}",
        request_method="GET",
    ),
    FrozenDict(
        title="Create a New Customer",
        doc="Create a new customer in the product with " +
        "productCode={product_code} and subscribe the customer to a " +
        "pricing plan",
        path="/customers/new/productCode/{product_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Import Customers",
        doc="Import customers to the product with productCode={product_code}" +
        ". Existing paying (or non-paying) customers in another billing " +
        "system may be imported while maintaining payment methods if the " +
        "billing solution is compatible.",
        path="/customers/import/productCode/{product_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Update a Customer and Subscription",
        doc="Update an existing customer's information in the product with " +
        "productCode={product_code} and modify the subscription information",
        path="/customers/edit/productCode/{product_code}/code/{customer_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Update a Customer Only",
        doc="Update an existing customer's information in the product with " +
        "productCode={product_code}",
        path="/customers/edit-customer/productCode/{product_code}/code/" +
        "{customer_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Update a Subscription Only",
        doc="Update an existing customer's subscription information in the " +
        "product with productCode={product_code}",
        path="/customers/edit-subscription/productCode/{product_code}/code/" +
        "{customer_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Delete a Customer",
        doc="Delete an existing customer in the product with productCode=" +
        "{product_code}",
        path="/customers/delete/productCode/{product_code}/code/" +
        "{customer_code}",
        request_method="GET",
    ),
    FrozenDict(
        title="Delete All Customers",
        doc="Delete all existing customers in the product with productCode=" +
        "{product_code}",
        path="/customers/delete-all/confirm/{current_unix_timestamp}" +
        "/productCode/{product_code}",
        request_method="GET",
    ),
    FrozenDict(
        title="Cancel a Customers Subscription",
        doc="Cancel an existing customer's subscription in the product with " +
        "productCode={product_code}",
        path="/customers/cancel/productCode/{product_code}/code/" +
        "{customer_code}",
        request_method="GET",
    ),
    FrozenDict(
        title="Add Item Quantity",
        doc="Increment a customer's current usage of a single item in the " +
        "product with productCode={product_code}",
        path="/customers/add-item-quantity/productCode/{product_code}/code/" +
        "{customer_code}/itemCode/{item_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Remove Item Quantity",
        doc="Decrement a customer's current usage of a single item in the " +
        "product with productCode={product_code}",
        path="/customers/remove-item-quantity/productCode/{product_code}" +
        "/code/{customer_code}/itemCode/{item_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Set Item Quantity",
        doc="Set a customer's current usage of a single item in the product " +
        "with productCode={product_code}",
        path="/customers/set-item-quantity/productCode/{product_code}/code/" +
        "{customer_code}/itemCode/{item_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Add a Custom Charge Credit",
        doc="Add an arbitrary charge or credit to the customer's current " +
        "invoice in the product with productCode={product_code}",
        path="/customers/add-charge/productCode/{product_code}/code/" +
        "{customer_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Delete a Custom Charge Credit",
        doc="Remove a charge or credit from the customer's current invoice " +
        "in the product with productCode={product_code}",
        path="/customers/delete-charge/productCode/{product_code}/code/" +
        "{customer_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Create a One time Invoice",
        doc="Create a parallel one-time invoice and execute the transaction " +
        "immediately using the customer's current payment method in the " +
        "product with productCode={product_code}",
        path="/invoices/new/productCode/{product_code}/code/{customer_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Run an Outstanding Invoice",
        doc="Execute an outstanding invoice in the product with " +
        "productCode={product_code}",
        path="/customers/run-outstanding/productCode/{product_code}/code/" +
        "{customer_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Issue a Refund",
        doc="Refund a transaction on a billed invoice in the product with " +
        "productCode={product_code}",
        path="/invoices/refund/productCode/{product_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Issue a Void",
        doc="Void a transaction on a billed invoice in the product with " +
        "productCode={product_code}",
        path="/invoices/void/productCode/{product_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Issue a Void or a Refund",
        doc="Defer to CheddarGetter to decide if a void or a refund is " +
        "executed against the invoice in the product with productCode=" +
        "{product_code}",
        path="/invoices/void-or-refund/productCode/{product_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Send an Invoice Email",
        doc="Send (or resend) email notification for the invoice in the " +
        "product with productCode={product_code}",
        path="/invoices/send-email/productCode/{product_code}",
        request_method="POST",
    ),
    FrozenDict(
        title="Get All Promotions",
        doc="Get all promotion data from the product with productCode=" +
        "{product_code}",
        path="/promotions/get/productCode/{product_code}",
        request_method="GET",
    ),
    FrozenDict(
        title="Get a Single Promotion",
        doc="Get the promotion data from the product with productCode=" +
        "{product_code} for the promotion with coupon code={coupon_code}",
        path="/promotions/get/productCode/{product_code}/code/{coupon_code}",
        request_method="GET",
    ),
)
