# 代码片段 维护中
class LibAI(MySpider):
    def __init__(self, sort_by=1, download_new=False, pic_path=r'C:\LibAI图片',
                 thunder_start_path=r"C:\Program Files (x86)\Thunder Network\Thunder\Program\ThunderStart.exe",
                 model_path=r'C:\迅雷下载',
                 **kwargs):
        """
        :param sort_by: 排序 推荐:0 最热:2 最新:1
        """
        super().__init__(**kwargs)
        self.sort_by = sort_by
        self.download_new = download_new
        self.mongo_init(database='spider', table='lib_ai_pictures')
        self.arithmetic = {
            'v1.5': "基础算法 v1.5",
            'v2.1': "基础算法 v2.1",
            'XL': "基础算法 XL",
            'a': "Cascade Stage a",
            'b': "Cascade Stage b",
            'c': "Cascade Stage c",
        }
        self.web_id = self.get_web_id()
        self.index_retry = 0
        self.total_get = 0
        self.finish = False
        self.file_path = pic_path
        self.model_path = model_path
        self.thunder_start_path = f'"{thunder_start_path}"'
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)
        if self.download_new:
            self.logger.info('当前为图片增量下载模式')


if __name__ == '__main__':
    liblib = LibAI()
    # 获取简略信息
    liblib.get_index()
    # 获取详情页信息
    liblib.get_page_info()
    # 下载缩略图
    liblib.download()
    # 整理模型链接
    liblib.get_model_url_to_mongo()
    # 下载模型
    liblib.download_model()
    # 更新模型下载状态
    liblib.update_model_download_status()
    # 重命名下载模型
    liblib.rename_model()
    # ……
