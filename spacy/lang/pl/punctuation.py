from ..char_classes import LIST_ELLIPSES, CONCAT_ICONS
from ..char_classes import CONCAT_QUOTES, ALPHA, ALPHA_LOWER, ALPHA_UPPER

_quotes = CONCAT_QUOTES.replace("'", "")

_infixes = (
    LIST_ELLIPSES
    + [CONCAT_ICONS]
    + [
        r"(?<=[{al}])\.(?=[{au}])".format(al=ALPHA_LOWER, au=ALPHA_UPPER),
        r"(?<=[{a}])[,!?](?=[{a}])".format(a=ALPHA),
        r"(?<=[{a}])[:<>=](?=[{a}])".format(a=ALPHA),
        r"(?<=[{a}])--(?=[{a}])".format(a=ALPHA),
        r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
        r"(?<=[{a}])([{q}\)\]\(\[])(?=[\-{a}])".format(a=ALPHA, q=CONCAT_QUOTES),
    ]
)

TOKENIZER_INFIXES = _infixes
