class MySpider:
    def __init__(
            self,
            proxies: bool = True,
            ua: bool = True,
            pools_start: bool = False,
            pools_number: int = 5,
            replace_ip_time_interval=10,
            auto_update_proxies=None,
            max_retries: int = 5,
            log_location=None
    ):
        """
        :param proxies:是否使用代理
        :param ua:是否使用随机UA
        :param auto_update_proxies:异常重试时是否自动更新代理
        :param pools_start:是否启动多线程
        :param pools_number:最大线程数量
        :param replace_ip_time_interval:线程间替换ip的最小时间间隔
        :param log_location:增加日志输出位置
        """
        self.headers = {}
        self.grid_fs = None
        self.proxies = None
        self.collection = None
        self.logger = logger
        self.pools_number = pools_number
        self.session = requests.session()
        self.ip_time = time.time() - 1000
        self.start_thread_pools = pools_start
        self.replace_ip_time_interval = replace_ip_time_interval
        self.use_proxies = proxies
        self.user_agent = ua
        if auto_update_proxies is None:
            self.auto_update_proxies = proxies
        else:
            self.auto_update_proxies = auto_update_proxies
        self.max_retries = max_retries
        if self.use_proxies:
            self.update_proxies()
        if self.user_agent:
            self.update_user_agent()
        if log_location is not None:
            self.logger.add(log_location,enqueue=True)
        if self.start_thread_pools:
            import threading
            from concurrent.futures import ThreadPoolExecutor
            pool = ThreadPoolExecutor()
        self.logger.debug(f'======= MySpider框架已启动 =======')
        self.logger.debug("=========== 初始化配置 ===========")
        self.logger.debug(f"代理：{'启用' if self.use_proxies else '未启用'}")
        self.logger.debug(f"随机UA：{'启用' if self.user_agent else '未启用'}")
        self.logger.debug(f"线程池：{'启用' if self.start_thread_pools else '未启用'}")
        if self.start_thread_pools:
            self.logger.debug(f"线程池大小：{self.pools_number}")
        self.logger.debug(f"IP更新间隔：{self.replace_ip_time_interval}秒")
        self.logger.debug(f"最大重试次数：{self.max_retries}")
        self.logger.debug("================================")
