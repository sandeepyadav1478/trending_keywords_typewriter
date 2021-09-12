# Swinging Keywords Writer

### - Scrap data from google

There are 2 files to do so, 1st is google-colab
and another is more fast and local machine code.

1) [colab link](https://colab.research.google.com/drive/1nIoFRBLoevumDFnm0MjlOCmnLldJDuQB?usp=sharing)

2) local machine code - scrap.py

#### Requirements

```python
pip install selenium keyboard pynput webdriver_manager
```

### - Type all keywords
Its a local machine code. Designed for agile usage and to keep it 'to point', there is no GUI interaction with app.
For start type-writing:<br/>
1) Change following in code:
  >
  > #-----------------------------
  >
  > keywords_import  = "assets/google_trend_keywords.csv"
  >
  > limit_words = 10
  >
  > exit_key = "esc"
  >
  > delay = 0   #in seconds
  >
  > #----------------------------
  > 
  I recommend that let delay remain 0, coz due to multiprocessing for force shutdown, code already writing in slow speed.
  
2) Run
    ```python
    py typewriter.py
    ```
    or
    ```python 
    python typewriter.py
    ```
3) Select option as mentioned in command palette

### Execution Sample

![Alt Text](https://github.com/sandeepyadav1478/trending_keywords_typewriter/blob/main/additional/My%20Video1.gif?raw=true)
