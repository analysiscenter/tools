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
            translation = self.translate_client.translate(cell.source, target_language='ru')
            # Google Translate adds a space between ] and ( and after some / in URLs
            cell.source = translation['translatedText'].replace('] (', '](').replace('/ ', '/')

        return cell, resources

class TranslateExporter(NotebookExporter):
    def __init__(self, config=None, **kwargs):
        super().__init__(config, **kwargs)
        self.register_preprocessor(TranslatePreprocessor, enabled=True)
