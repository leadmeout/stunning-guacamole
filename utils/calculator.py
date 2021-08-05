CLASSIFICATION_DICT = {
    'ch': 'EU',
    'de': 'EU',
    'fr': 'EU',
    'us': 'US'
}


INTERNAL_TAX_DICT = {
    'de': 0.19,
    'ch': 0.077,
    'us': 0,
}

TAX_RATE_LIST = [
    (0.19, '19%'),
    (0.077, '7.7%'),
    (0, 'Steuerfrei')
]

def result_generator(sender, receiver, net_total):
    net_total = float(net_total)
    tax = float(INTERNAL_TAX_DICT[receiver])
    gross_total = net_total * tax + net_total
    designation = CLASSIFICATION_DICT[receiver]

    yield tax
    yield gross_total
    yield designation


def get_tax_rate(receiver):
    return float(INTERNAL_TAX_DICT[receiver])

def get_gross(receiver, net_total):
    tax = float(INTERNAL_TAX_DICT[receiver])
    gross_total = net_total * tax + net_total
    return gross_total

def get_classification(receiver):
    return CLASSIFICATION_DICT[receiver]
