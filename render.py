from ghostpy import Compiler
from ghostpy._compiler import _ghostpy_

class Renderer:

    def __init__(self, theme):
        self.theme = theme
        self.compiler = Compiler(theme)

    def render(self, file, dict_):
        blog_dict = {
            'url': 'url.com',
            'title': 'Test Title',
            'description': 'Test description',
            'navigation': [{
                'label': 'Test',
                'url': 'test.com',
                'current': True,
                'slug': 'Test'
            }, {
                'label': 'Test2',
                'url': 'test2.com',
                'current': False,
                'slug': 'Test2'
            }, {
                'label': 'Test3',
                'url': 'test3.com',
                'current': False,
                'slug': 'Test3'
            }]
        }
        with open(file) as hbs:
            source = hbs.read().decode('unicode-escape')
        _dict = dict(dict_, **blog_dict)
        _ghostpy_['blog_dict'] = _dict
        template = self.compiler.compile(source)
        output = template(_dict)
        return output
