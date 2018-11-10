import os


class Utils(object):
    #创建一个目录
    @staticmethod
    def mkdir(dirWithFullPath):
        if not os.path.exists(dirWithFullPath):
            # 可创建不存在的父目录
            os.makedirs(dirWithFullPath)
        else:
            pass