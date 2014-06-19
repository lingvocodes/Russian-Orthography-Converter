import codecs, re

def generalSwap(fname):
    fIn = codecs.open(fname, 'r', 'utf-8')
    for line in fIn:
        line = re.sub(u'ѣ', u'е', line)
        line = re.sub(u'ьи', u'ье', line)
        line = re.sub(u'аго\\b', u'ого', line)
        line = re.sub(u'яго\\b', u'его', line)
        line = re.sub(u'ъ', '', line)
        line = re.sub(u'\\b([Оо])не\\b', u'\\1ни', line, flags = re.U)
        line = re.sub(u'\\b([Чч])о', u'\\1е', line, flags = re.U)
        line = re.sub(u'ѳ', u'ф', line)
        line = re.sub(u'\\bея\\b', u'ее', line, flags = re.U)
        line = re.sub(u'ъ', '', line)
        line = re.sub(u'iю', u'ью', line)
        line = re.sub(u'iя', u'ия', line)
        line = re.sub(u'iэ', u'ие', line)
        return line
def prefixSwap(fname):
    dSOGL = {u'без': u'бес', u'из': u'ис',
                 u'раз': u'рас',u'роз': u'рос',
                u'низ': u'нис',u'через': u'черес'}
    fIn = codecs.open(fname, 'r', 'utf-8')
    for line in fIn:
        line = re.sub(u'([пП])олу(\w+\\b)', u'\\1олу\\1', line,\
                          flags = re.U)
        for k, v in dSOGL.items():
            line = re.sub('\\b' + k + u'([кпстфхцчшщ])' + '(\\w+)', v + '\\1' + \
                              '\\2', line, flags = re.U)
    return line
def dicSwap(fname):
    fIn = codecs.open(fname, 'r', 'utf-8')
    for line in fIn:
        line = re.sub(u'([иИ])тти', u'\\1дти', line)
        line = re.sub(u'([Чч])\.(кер \\w*)', u'\\1о\\2', line, flags = re.U)
        line = re.sub(u'([Сс]ерiозно)', u'\\1ерьезно', line)
        line = re.sub(u'([Мм])аioр', u'\\1айор', line)
        line = re.sub(u'ыя', u'ые', line, flags = re.U)
        line = re.sub(u'([Сс])трые', u'\\1ыя', line, flags = re.U)
        line = re.sub(u'([Вв])ые', u'\\1ыя', line, flags = re.U)
        line = re.sub(u'([Бб])атые', u'\\1ыя', line, flags = re.U)
        return line

def fullSwap(fname):
    dicSwap(prefixSwap((generalSwap(name))))


print dicSwap('in.txt')   
    
