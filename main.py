# coding: utf-8
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image

from config import WordCloudConfig as cfg


def get_mask():
    # 想要文字雲出現的圖示
    if cfg.WITH_MASK:
        mask = np.array(Image.open(cfg.MASK_PATH))
        # create coloring from image
        image_colors = ImageColorGenerator(mask)
        return mask, image_colors
    return None, None


def build_word_cloud(terms, mask):
    # 背景顏色預設黑色，改為白色
    wordcloud = WordCloud(background_color=cfg.BG_COLOR, mask=mask, font_path=cfg.FONT,
                          collocations=False, width=2400, height=2400, margin=2)
    wordcloud.generate_from_frequencies(frequencies=Counter(terms))
    return wordcloud


def make_and_save_figure(wordcloud, image_colors):
    # 產生圖片
    plt.figure(figsize=(20, 20), facecolor='k')
    if cfg.WITH_MASK:
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
    else:
        plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)

    # 顯示用
    # plt.show()

    plt.savefig(cfg.PIC_PATH)


def generate_new_word_cloud(terms):
    mask, image_colors = get_mask()
    wordcloud = build_word_cloud(terms, mask)
    make_and_save_figure(wordcloud, image_colors)


if __name__ == '__main__':
    cfg.WC_DIR.mkdir(parents=True, exist_ok=True)
    import random
    char_list = list(range(ord('A'), ord('z')))  # data here, list of tokenized words
    my_terms = []
    for c in char_list:
        my_terms.extend([chr(c)] * random.randint(0, 50))

    generate_new_word_cloud(my_terms)
