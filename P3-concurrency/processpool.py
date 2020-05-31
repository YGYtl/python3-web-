#线程池
import time
from multiprocessing import Pool
from common import setup_down_path, get_links, download_one
from logger import logger

def download_many():
    '''多进程，按进程数 并行 下载所有图片
    使用multiprocessing.Pool.apply_async()
    '''
    down_path = setup_down_path()
    links = get_links()

    p = Pool(4)
    for linkno, link in enumerate(links,1):
        image = {
            'path': down_path,
            'linkno': linkno,
            'link': link
        }
        p.apply_async(download_one,args=(image,))
    logger.info('Waiting for all subprocesses done...')
    p.close()
    p.join()
    logger.info('All subprocesses done.')

    return len(links)

if __name__ == '__main__':
    t0 = time.time()
    count = download_many()
    msg = '{} flags downloaded in {} seconds.'
    logger.info(msg.format(count, time.time() - t0))