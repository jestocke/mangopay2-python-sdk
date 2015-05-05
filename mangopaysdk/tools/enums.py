class RequestType:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class PersonType:
    Natural = 'NATURAL'
    Legal = 'LEGAL'


class LegalPersonType:
    BUSINESS = 'BUSINESS'
    ORGANIZATION = 'ORGANIZATION'


class TransactionStatus:
    CREATED = 'CREATED'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'


class TransactionType:
    PAYIN = 'PAYIN'
    PAYOUT = 'PAYOUT'
    TRANSFER = 'TRANSFER'


class TransactionStatus:
    CREATED = 'CREATED'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'


class PayInPaymentType:
    CARD = 'CARD'
    BANK_WIRE = 'BANK_WIRE'
    AUTOMATIC_DEBIT = 'AUTOMATIC_DEBIT'
    DIRECT_DEBIT = 'DIRECT_DEBIT'


class ExecutionType:
    WEB = 'WEB'
    DIRECT = 'DIRECT'
    PREAUTHORIZED = 'PREAUTHORIZED'


class PayOutPaymentType:
     BANK_WIRE = 'BANK_WIRE'


class Mode3DSType:
    DEFAULT = 'DEFAULT'
    FORCE = 'FORCE'


class CardType:
    CB_VISA_MASTERCARD = 'CB_VISA_MASTERCARD'
    AMEX = 'AMEX'
    DINERS = 'DINERS'
    MAESTRO = 'MAESTRO'
    MASTERPASS = 'MASTERPASS'


class TransactionNature:
    REGULAR = 'REGULAR'
    REFUND = 'REFUND'
    REPUDIATION = 'REPUDIATION'


class CardRegistrationStatus:
    CREATED = 'CREATED'
    ERROR = 'ERROR'
    VALIDATED = 'VALIDATED'

class CardPreAuthorizationStatus:
    WAITING = 'WAITING'
    CANCELED = 'CANCELED'
    EXPIRED = 'EXPIRED'
    VALIDATED = 'VALIDATED'

class EventType:
    PAYIN_NORMAL_CREATED = 'PAYIN_NORMAL_CREATED'
    PAYIN_NORMAL_SUCCEEDED = 'PAYIN_NORMAL_SUCCEEDED'
    PAYIN_NORMAL_FAILED = 'PAYIN_NORMAL_FAILED'
    PAYOUT_NORMAL_CREATED = 'PAYOUT_NORMAL_CREATED'
    PAYOUT_NORMAL_SUCCEEDED = 'PAYOUT_NORMAL_SUCCEEDED'
    PAYOUT_NORMAL_FAILED = 'PAYOUT_NORMAL_FAILED'
    TRANSFER_NORMAL_CREATED = 'TRANSFER_NORMAL_CREATED'
    TRANSFER_NORMAL_SUCCEEDED = 'TRANSFER_NORMAL_SUCCEEDED'
    TRANSFER_NORMAL_FAILED = 'TRANSFER_NORMAL_FAILED'
    PAYIN_REFUND_CREATED = 'PAYIN_REFUND_CREATED'
    PAYIN_REFUND_SUCCEEDED = 'PAYIN_REFUND_SUCCEEDED'
    PAYIN_REFUND_FAILED = 'PAYIN_REFUND_FAILED'
    PAYOUT_REFUND_CREATED = 'PAYOUT_REFUND_CREATED'
    PAYOUT_REFUND_SUCCEEDED = 'PAYOUT_REFUND_SUCCEEDED'
    PAYOUT_REFUND_FAILED = 'PAYOUT_REFUND_FAILED'
    TRANSFER_REFUND_CREATED = 'TRANSFER_REFUND_CREATED'
    TRANSFER_REFUND_SUCCEEDED = 'TRANSFER_REFUND_SUCCEEDED'
    TRANSFER_REFUND_FAILED = 'TRANSFER_REFUND_FAILED'
    KYC_CREATED = 'KYC_CREATED'
    KYC_VALIDATION_ASKED = 'KYC_VALIDATION_ASKED'
    KYC_SUCCEEDED = 'KYC_SUCCEEDED'
    KYC_FAILED = 'KYC_FAILED'

class KycDocumentType:
    IDENTITY_PROOF = 'IDENTITY_PROOF'
    REGISTRATION_PROOF = 'REGISTRATION_PROOF'
    ARTICLES_OF_ASSOCIATION = 'ARTICLES_OF_ASSOCIATION'
    SHAREHOLDER_DECLARATION = 'SHAREHOLDER_DECLARATION'
    ADDRESS_PROOF = 'ADDRESS_PROOF'

class KycDocumentStatus: 	
    CREATED = 'CREATED'
    VALIDATION_ASKED = 'VALIDATION_ASKED'
    VALIDATED = 'VALIDATED'
    REFUSED = 'REFUSED'

class SortDirection:
    DESC = 'desc'
    ASC = 'asc'

class InitialTransactionType:
    PAYIN = 'PAYIN'
    PAYOUT = 'PAYOUT'
    TRANSFER = 'TRANSFER'

class RefundReasonType:
    BANKACCOUNT_INCORRECT = 'BANKACCOUNT_INCORRECT'
    BANKACCOUNT_HAS_BEEN_CLOSED = 'BANKACCOUNT_HAS_BEEN_CLOSED'
    OWNER_DOT_NOT_MATCH_BANKACCOUNT = 'OWNER_DOT_NOT_MATCH_BANKACCOUNT'
    WITHDRAWAL_IMPOSSIBLE_ON_SAVINGS_ACCOUNTS = 'WITHDRAWAL_IMPOSSIBLE_ON_SAVINGS_ACCOUNTS'
    INITIALIZED_BY_CLIENT = 'INITIALIZED_BY_CLIENT'
    OTHER = 'OTHER'

class KYCLevel:
    LIGHT = 'LIGHT'
    REGULAR = 'REGULAR'

class DepositAccountType:
    CHECKING = 'CHECKING'
    SAVINGS = 'SAVINGS'

#class AuthenticationType:
#    Basic = 'Basic'
#    Strong = 'Strong'
