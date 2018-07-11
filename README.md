# darksky ML

Code based on examples in
https://stackabuse.com/using-machine-learning-to-predict-the-weather-part-1/.
Wunderground no longer has an open API, so darksky's API is being used
instead.

## Installation
```bash
pip install -r requirements.txt
cp .env{.example,}
vim .env # update with darksky api key
python main.py
```
