# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
from scipy.misc import imread

coloring = np.array(Image.open("chcidraky_icon.png"))

more_stopwords = {
    'na',
    'se',
    'image',
    'black',
    u'kč',
    'cm',
    'cca',
    u'šířka',
    u'délka',
    u'výška',
    u'balení',
    u'složení',
    u'rozměry',
    u'vás',
    u'obvod',
    u'sa',
    u'jedná',
    u'proti',
    u'musí',
}
STOPWORDS = STOPWORDS.union(more_stopwords)

with open('cs_stopwords.txt', 'r') as f:
    cs_stopwords = f.read().decode('utf-8')
    for word in cs_stopwords.split():
        STOPWORDS.add(word.strip())

with open('data.txt', 'r') as f:
    packages = f.read().decode('utf-8')

wordcloud = WordCloud(
                      #font_path='flux.ttf',
                      stopwords=STOPWORDS,
                      background_color='black',
                      width=1000,
                      height=1000,
                      mask=coloring
                     ).generate(packages)

image_colors = ImageColorGenerator(coloring)


# show
plt.figure()
# recolor wordcloud and show
plt.imshow(wordcloud.recolor(color_func=image_colors))
plt.axis("off")
plt.show()
