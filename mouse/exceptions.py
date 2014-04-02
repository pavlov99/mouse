""" Cheddargetter exceptions.

    List of exeptions with codes:
    http://support.cheddargetter.com/kb/api-8/error-handling#error-codes

"""
from . import six


class CheddargetterExceptionMeta(type):

    """ Metaclass from Exception Factory."""

    __store__ = dict()

    def __new__(class_, name, bases, params):
        cls = super(CheddargetterExceptionMeta, class_).__new__(
            class_, name, bases, params)
        class_.__store__[(cls.CODE, cls.AUX_CODE)] = cls
        return cls


@six.add_metaclass(CheddargetterExceptionMeta)
class CheddargetterException(Exception):

    """ Base class for Cheddargetter exceptions."""

    CODE = None
    AUX_CODE = None

    def __init__(self, id, message, code=None, auxCode=None):
        self.id = id
        self.message = message
        self.code = self.CODE or code
        self.auxCode = self.AUX_CODE or auxCode

    @classmethod
    def instantiate(cls, **kwargs):
        code = kwargs.get("code")
        auxCode = kwargs.get("auxCode")
        code = int(code) if code else None
        auxCode = int(auxCode) if auxCode else None
        kwargs["code"] = code
        kwargs["auxCode"] = auxCode
        key = (code, auxCode)
        class_ = cls.__store__.get(key) or CheddargetterException
        return class_(**kwargs)


class CheddargetterBadRequest(CheddargetterException):
    CODE = 400


class CheddargetterRecordExists(CheddargetterBadRequest):
    CODE = 400
    AUX_CODE = 1001


class CheddargetterNotAuthorized(CheddargetterException):
    CODE = 401


class CheddargetterGatewayConfigurationIncompatible(
        CheddargetterNotAuthorized):
    CODE = 401
    AUX_CODE = 2000


class CheddargetterConfigurationAtGatewayIncompatible(
        CheddargetterNotAuthorized):
    CODE = 401
    AUX_CODE = 2001


class CheddargetterAuthenticationGatewayFailed(CheddargetterNotAuthorized):
    CODE = 401
    AUX_CODE = 2002


class CheddargetterGatewayAccessDenied(CheddargetterNotAuthorized):
    CODE = 401
    AUX_CODE = 2003


class CheddargetterGatewayNotSupportRequestedAction(
        CheddargetterNotAuthorized):
    CODE = 401
    AUX_CODE = 2004


class CheddargetterNotFound(CheddargetterException):
    CODE = 404


class CheddargetterPreconditionFailed(CheddargetterException):
    CODE = 412


class CheddargetterUnprocessableEntity(CheddargetterException):
    CODE = 422


class CheddargetterErrorProcessingTransaction(
        CheddargetterUnprocessableEntity):
    CODE = 422
    AUX_CODE = 5000


class CheddargetterCreditCardNumberInvalid(CheddargetterUnprocessableEntity):
    CODE = 422
    AUX_CODE = 5001


class CheddargetterExpirationDateInvalid(CheddargetterUnprocessableEntity):
    CODE = 422
    AUX_CODE = 5002


class CheddargetterCreditCardTypeNotAccepted(CheddargetterUnprocessableEntity):
    CODE = 422
    AUX_CODE = 5003


class CheddargetterTransactionDeclined(CheddargetterUnprocessableEntity):
    CODE = 422
    AUX_CODE = 6000


class CheddargetterTransactionDeclinedAVSMismatch(
        CheddargetterUnprocessableEntity):
    CODE = 422
    AUX_CODE = 6001


class CheddargetterTransactionDeclinedCardCodeVerification(
        CheddargetterUnprocessableEntity):
    CODE = 422
    AUX_CODE = 6002


class CheddargetterTransactionDeclinedInsufficientFund(
        CheddargetterUnprocessableEntity):
    CODE = 422
    AUX_CODE = 6003


class CheddargetterCreditCardNumberInvalidDeclined(
        CheddargetterUnprocessableEntity):
    CODE = 422
    AUX_CODE = 6004


class CheddargetterCreditCardTypeNotAcceptedDeclined(
        CheddargetterUnprocessableEntity):
    CODE = 422
    AUX_CODE = 6005


class CheddargetterTransactionFailedUnknownReason(
        CheddargetterUnprocessableEntity):
    CODE = 422
    AUX_CODE = 7000


class CheddargetterInternalServerError(CheddargetterException):
    CODE = 500


class CheddargetterUnrecognizedGatewayError(CheddargetterInternalServerError):
    CODE = 500
    AUX_CODE = 1000


class CheddargetterInvalidCommunication(CheddargetterInternalServerError):
    CODE = 500
    AUX_CODE = 1002


class CheddargetterRecordNotFound(CheddargetterInternalServerError):
    CODE = 500
    AUX_CODE = 1003


class CheddargetterBadGateway(CheddargetterException):
    CODE = 502


class CheddargetterGatewayResponseNotRecognized(CheddargetterBadGateway):
    CODE = 502
    AUX_CODE = 3000


class CheddargetterGatewayConnectionFailed(CheddargetterBadGateway):
    CODE = 502
    AUX_CODE = 4000


class CheddargetterServiceUnavailable(CheddargetterException):
    CODE = 503
