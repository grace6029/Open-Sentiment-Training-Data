# Open Sentiment Training Data

有鑑於Training Data實在太難找了，所以乾脆自己做一個然後公開  
期望大家都能夠共享自己的Training Data  
讓 Sentiment Analysis 能更進一步~

## Models語料大小

* pos.txt：309163筆，44M
* neg.txt：320456筆，15M

## Models成份
以下資料皆濾掉標題包含 `[公告]` 的文章
* `pos.txt` 正面情緒的model，包含：  
  * adulation版：標題 + 內文
  * dreams-wish版：標題 + 內文
  * happy版：標題 + 內文（每一句都斷句）
  * kindness版：標題 + 內文裡面的`好人行為`區段的文字
  * luchky版：標題
* `neg.txt` 負面情緒的model，包含：  
  * broken-heart版：標題 + 內文
  * HatePolitics版：標題 + 內文（只有包含黑特且不包含RE的才納入）
  * pity版：標題 + 內文
  * sad版：標題 + 內文（每一句都斷句）
  * sorry版：標題 + 內文
