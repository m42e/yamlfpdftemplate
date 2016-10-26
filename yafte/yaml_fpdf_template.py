# YamlFPDFTemplate
# 
# Allows to define a template in yaml
from fpdf import Template
import yaml

class MissingParameterError(Exception):
    pass

class YaFTe(Template):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.tconfig = yaml.load(f.read())
            self.tconfig.pop('templates', {})
        super().__init__(**self.tconfig.pop('docoptions', {}), elements=self.prepare_elements())
    
    def prepare_elements(self):
        elements = []
        defaults = self.tconfig.pop('defaults', {})
        for key, telement in self.tconfig.items():
            elem = defaults.copy()
            elem.update(telement)
            elem['name'] = key

            try:
                def setreplace(dct, key, replace):
                    if not key in dct:
                        dct[key] = replace(dct)

                setreplace(elem, 'x1', lambda x: x.pop('x'))
                setreplace(elem, 'y1', lambda x: x.pop('y'))
                setreplace(elem, 'x2', lambda x: x['y1'] + x.pop('w'))
                setreplace(elem, 'y2', lambda x: x['y1'] + x.pop('h'))
            except KeyError as ke:
                raise MissingParameterError('element {0} configuration incorrect'.format(key)) from ke

            elements.append(elem)
        return elements
