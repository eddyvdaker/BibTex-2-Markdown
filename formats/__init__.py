"""
    bibtex2md.formats
    ~~~~~~~~~~~~~~~~~

    This package contains the different formats to which the references can
    be formatted. This file also contains the base formats class.

    Author  : Eddy van den Aker
    License : MIT
"""


class Base:

    @staticmethod
    def generate_reference_list(references):
        return ""


from formats.APA6 import APA6

formats_list = {'APA6': APA6}
