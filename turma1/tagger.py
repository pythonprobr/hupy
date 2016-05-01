"""
A funcao `tag` devolve um elemento HTML.

    >>> tag('br')
    '<br />'
    >>> tag('pre', 'bla')
    '<pre>bla</pre>'
    >>> tag('p', 'Bom dia!', cls='piscando')
    '<p class="piscando">Bom dia!</p>'
    >>> tag('p', cls='piscando', conteudo='Boa noite!')
    '<p class="piscando">Boa noite!</p>'
    >>> tag('p', cls='piscando', conteudo='Boa noite!', id=678)
    '<p class="piscando" id="678">Boa noite!</p>'
    >>> tag('div', 'foo', src='manga.jpg', width='200', height='300')
    '<div height="300" src="manga.jpg" width="200">foo</div>'
    >>> tag('div', 'foo', src='manga.jpg', id=127, width='200', height='300')
    '<div height="300" id="127" src="manga.jpg" width="200">foo</div>'

"""

def tag(nome, conteudo=None, cls=None, **atributos):
    """Generate one or more HTML tags"""
    if cls is not None:
        atributos['class'] = cls
    if atributos:
        atr_str = ''.join(' %s="%s"' % (atr, valor)
                           for atr, valor
                           in sorted(atributos.items()))
    else:
        atr_str = ''
    if conteudo is None:
        return '<{}{} />'.format(nome, atr_str)
    else:
        return '<{0}{1}>{2}</{0}>'.format(nome, atr_str, conteudo)
