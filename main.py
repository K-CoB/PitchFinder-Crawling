from lib.database import create_music_in_mysql
from lib.music import crawl_music
from utils.validate import validate_data


def process():
    data = crawl_music()
    data = validate_data(data)

    print(data)
    create_music_in_mysql(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
