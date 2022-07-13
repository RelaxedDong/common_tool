import random
import string


def generate_invite_code(length):
    letters = list(string.ascii_letters)
    letters.extend(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    return ''.join(random.sample(letters, length)).upper()


def generate_number_code(count):
    # 定义一个种子，从这里面随机拿出一个值，可以是字母
    seeds = "1234567890"
    # 定义一个空列表，每次循环，将拿到的值，加入列表
    random_num = []
    # choice函数：每次从seeds拿一个值，加入列表
    for i in range(count):
        random_num.append(random.choice(seeds))
    # 将列表里的值，变成四位字符串
    return "".join(random_num)


def random_unique_selects(population, need_count=1):
    """
    序列随机选择
    :param population:
    :param need_count:
    :return:
    """
    if not population:
        return []
    return random.sample(population, min(need_count, len(population)))


def generate_file_name(random_str_count=20):
    """
    随机生成图片名
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
    return ''.join(random.sample(alphabet, random_str_count)) + '.jpg'
