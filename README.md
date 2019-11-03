# WordCloud 文字雲
A simple word cloud inplementation.
不多說，文字雲是最好的詞頻視覺化功能！

## Coding
### 主程式 `main.py`
1. Build a list of terms 建立文字清單
```python3
terms = ['我', '我', '是', '一顆', '文字雲', '文字雲', '我']
```
2. make mask (optional) 想要文字雲出現的圖示

會輸出圖片的圖片形狀遮罩mask及顏色遮罩image_colors

```python3
mask, image_colors = get_mask()
```

3. build the word cloud by given terms and mask 建立文字雲
```python3
wordcloud = build_word_cloud(terms, mask)
```

4. make the figure and save as file 製成圖片格式並輸出

顏色遮罩可以在這邊設定
```python3
make_and_save_figure(wordcloud, image_colors)
```

### Configuration `config.py`



## References
- http://stacepsho.blogspot.com/2018/06/word-cloud-in-python.html
