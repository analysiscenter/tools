""" Contains jupyter notebook exporter that translates markdown cells to Russian language """
from google.cloud import translate
from nbconvert.preprocessors import Preprocessor
from nbconvert.exporters.notebook import NotebookExporter


class TranslatePreprocessor(Preprocessor):
    """ Translate all Markdown cells to Russian """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.translate_client = translate.Client()

    def preprocess_cell(self, cell, resources, index):
        """ Translate all Markdown cells to Russian """

        if 'source' in cell and cell.cell_type == "markdown":
            # Google Translate API does not preserve newline symbol and 
            # leading spaces (useful to keep nested lists)
            lines = cell.source.split('\n')
            translated_lines = [' ' * (len(line) - len(line.lstrip(' '))) +
                                self.translate_client.translate(line, target_language='ru')['translatedText']
                                for line in lines]
            translation = '\n'.join(translated_lines)
            # Google Translate adds a space between ] and ( and after some / in URLs
            cell.source = translation.replace('] (', '](').replace('/ ', '/')

        return cell, resources

class TranslateExporter(NotebookExporter):
    def __init__(self, config=None, **kwargs):
        super().__init__(config, **kwargs)
        self.register_preprocessor(TranslatePreprocessor, enabled=True)
