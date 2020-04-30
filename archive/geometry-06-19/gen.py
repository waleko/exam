import os
import codecs


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


f = open("que.txt", "r")
data = f.read()
lines = data.split('\n')
for line in lines:
    dot_pos = line.index('.')
    num = int(line[:dot_pos])
    text = line[dot_pos + 2:]
    short_size = 50
    short_text = text[:short_size]
    if len(text) > short_size and short_size != -1:
        short_text += '...'
    createFolder(str(num))
    with codecs.open(str(num) + '/README.md', 'w+', encoding='utf-8') as f:
        data_to_write = '# Билет №' + str(num) + '\n' + text + '\n\n\n'
        f.write(data_to_write)
    print('* [Билет №' + str(num) + ' (' + short_text + ')](' + str(num) + ')')
print('--------------')
print('Done!')
