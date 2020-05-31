from common import setup_down_path, get_links, download_one_starmap
import time
from logger import logger
from multiprocessing import Pool

def download_many_starmap():
    '''
    多进程，按进程数 并行 下载所有图片
    使用multiprocessing.Pool.starmap(download_one_starmap, images)，它是Python-3.3添加的
    可以给download_one_starmap()函数传元组组成的序列，会自动解包元组给函数的多个参数
    '''
    down_path = setup_down_path()
    links = get_links()

    images = []
    for linkno, link in enumerate(links, 1):
        images.append((down_path, linkno, link))

    with Pool(4) as p:
        p.starmap(download_one_starmap, images) #链接带序号

    logger.info('Waiting for all subprocesses done...')
    logger.info('All subprocesses done.')

    return len(links)

if __name__ == '__main__':
    t0 = time.time()
    count = download_many_starmap()
    msg = '{} flags downloaded in {} seconds.'
    logger.info(msg.format(count, time.time() - t0))