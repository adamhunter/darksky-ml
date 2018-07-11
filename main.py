from dotenv import load_dotenv, find_dotenv
from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime, timedelta
import pandas as pd

from darksky.download import maybe_download
from darksky.data import parse_all, features

def main():
    print("running!")
    load_dotenv(find_dotenv())
    date = datetime(2015, 1, 1)
    days = range(0, 991)
    dates = [date + timedelta(days=i) for i in days]
    with ThreadPoolExecutor(5) as executor:
        futures = [executor.submit(maybe_download, d) for d in dates]
        wait(futures)
    records = parse_all(dates)

    # df = pd.DataFrame(records, columns=features).set_index('date')  

    print(records)
    # tmp = df[['maxtemp', 'mintemp', 'meandewpt']].head(10)  
    # print(tmp)


if __name__ == '__main__':
    main()
