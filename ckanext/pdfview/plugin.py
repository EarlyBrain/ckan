import logging
import ckan.plugins as p

log = logging.getLogger(__name__)
ignore_empty = p.toolkit.get_validator('ignore_empty')

DEFAULT_PDF_FORMATS = ['pdf']


class PdfView(p.SingletonPlugin):
    '''This plugin makes views of pdf resources, using an <iframe> tag'''

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'theme/templates')

    def info(self):
        return {'name': 'pdf_view',
                'title': p.toolkit._('Data Explorer'),
                'icon': 'file-text-alt',
                'schema': {'image_url': [ignore_empty, unicode]},
                'iframed': False,
                'always_available': True,
                'default_title': p.toolkit._('Data Explorer'),
                }

    def can_view(self, data_dict):
        return (data_dict['resource'].get('format', '').lower()
                in DEFAULT_PDF_FORMATS)

    def view_template(self, context, data_dict):
        return 'pdf_view.html'
