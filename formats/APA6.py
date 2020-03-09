"""
    bibtex2md.formats.APA6
    ~~~~~~~~~~~~~~~~~~~~~~

    APA6 style for the references list.

    Author  : Eddy van den Aker
    License : MIT
"""
from formats import Base


class APA6(Base):

    @staticmethod
    def format_date(reference):
        date_txt = '('
        if 'year' in reference:
            date_txt += reference['year']
            if 'month' in reference:
                date_txt += f', {reference["month"]}'
                if 'day' in reference:
                    date_txt += f' {reference["day"]}'
        else:
            date_txt += 'n.d.'
        return date_txt + ').'

    @staticmethod
    def format_author_date_title(reference):
        adt_txt = ''
        if 'author' in reference:
            adt_txt += reference["author"].replace('and', '&') \
                + f' {APA6.format_date(reference)}' \
                + f' {reference["title"]}.'
        else:
            adt_txt += reference['title'] + f' {APA6.format_date(reference)}'
        return adt_txt
    
    @staticmethod
    def strip_newlines(references):
        for i, ref in enumerate(references):
            for key, value in ref.items():
                ref[key] = value\
                    .replace('\n', ' ')\
                    .replace('\t', '')\
                    .replace('\\', '')
        return references

    @staticmethod
    def generate_reference_list(references):
        refs = []
        references = APA6.strip_newlines(references)
        for ref in references:
            refs.append(APA6.format_reference(ref))

        refs_txt = ''
        refs.sort()
        for ref in refs:
            refs_txt += f'{ref}\n\n'\
                .replace('{', '')\
                .replace('}', '')\
                .replace('..', '.')
        return refs_txt[:-4]

    @staticmethod
    def format_reference(reference):
        entry_type = reference['ENTRYTYPE']
        if entry_type == 'inproceedings':
            return APA6.article_proceeding_format(reference)
        elif entry_type == 'article':
            return APA6.article_proceeding_format(reference)
        elif entry_type == 'book':
            return APA6.book_format(reference)
        else:
            return APA6.default_format(reference)

    @staticmethod
    def default_format(reference):
        ref_txt = f'{APA6.format_author_date_title(reference)}.'
        if 'url' in reference:
            ref_txt += reference['url']
        return ref_txt

    @staticmethod
    def article_proceeding_format(reference):
        ref_txt = APA6.format_author_date_title(reference)
        if 'journal' in reference:
            ref_txt += f' {reference["journal"]}'
        if 'volume' in reference:
            ref_txt += f', {reference["volume"]}'
        if 'pages' in reference:
            ref_txt += f', {reference["pages"]}.'
        if 'url' in reference:
            ref_txt += f' {reference["url"]}'
        elif 'doi' in reference:
            ref_txt += f' {reference["doi"]}'
        return ref_txt

    @staticmethod
    def book_format(reference):
        ref_txt = APA6.format_author_date_title(reference)
        if 'publisher' in reference:
            ref_txt += f' {reference["publisher"]}.'
        if 'url' in reference:
            ref_txt += f' {reference["url"]}'
        elif 'doi' in reference:
            ref_txt += f' {reference["doi"]}'
        return ref_txt
