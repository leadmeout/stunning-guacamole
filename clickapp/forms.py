from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from utils.calculator import get_classification, get_gross, get_tax_rate, result_generator


class TariffCalcForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Calculate'))

    WAREHOUSE_LIST = [
        ('de', 'DE'),
        ('ch', 'CH')
    ]

    CUSTOMER_LIST = [
        ('de', 'DE'),
        ('ch', 'CH'),
        ('fr', 'FR'),
        ('us', 'US')
    ]

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

    TAX_RATE_DICT = {
        0.19: '19%',
        0.077: '7.7%',
        0: 'Steuerfrei'
    }

    warehouse = forms.CharField(
        label=False, widget=forms.Select(choices=WAREHOUSE_LIST))
    customer = forms.CharField(
        label=False, widget=forms.Select(choices=CUSTOMER_LIST))
    net = forms.DecimalField(label=False, decimal_places=2)
    tax_rate = forms.CharField(
        label=False, disabled=True, required=False)
    gross = forms.CharField(label=False, disabled=True, required=False)
    classification = forms.CharField(
        label=False, disabled=True, required=False)

    @property
    def get_tax_rate(self):
        try:
            tax = self.INTERNAL_TAX_DICT[self.cleaned_data['customer']]
        except KeyError:
            tax = self.INTERNAL_TAX_DICT[self.cleaned_data['warehouse']]
        return self.TAX_RATE_DICT[tax]

    @property
    def get_gross(self):
        receiver = self.cleaned_data['customer']
        net_total = float(self.cleaned_data['net'])
        try:
            tax = float(self.INTERNAL_TAX_DICT[receiver])
        except KeyError:
            tax = float(self.INTERNAL_TAX_DICT[self.cleaned_data['warehouse']])
        gross_total = round(net_total * tax + net_total, 2)
        return f"{gross_total:.2f}"

    @property
    def get_classification(self):
        receiver = self.cleaned_data['customer']
        return self.CLASSIFICATION_DICT[receiver]
