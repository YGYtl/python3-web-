import time
from multiprocessing import Pool
from common import setup_down_path, get_links, download_one
from logger import logger

def download_many_map():
    '''
    多进程，按进程数 并行 下载所有图片
    使用 multiprocessing.Pool.map(download_one, images)
    主义Pool.map限制了download_one()只能接受一个参数，所以images是字典构成的列表
    '''
    down_path = setup_down_path()
    links = get_links()
    images = []

    for linkno, link in enumerate(links, 1):
        image = {
            'path': down_path,
            'linkno': linkno,
            'link': link
        }
        images.append(image)
    with Pool(4) as p:
        p.map(download_one,images)
    #使用with，能够自动调用Pool.close()和Pool.join()
    
    logger.info('Waiting for all subprocesses done...')
    return len(links)

if __name__ == '__main__':
    t0 = time.time()
    count = download_many_map()
    msg = '{} flags downloaded in {} seconds.'
    logger.info(msg.format(count, time.time() - t0))