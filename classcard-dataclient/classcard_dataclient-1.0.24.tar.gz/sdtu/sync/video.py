from sync.base import BaseSync
from spider.video import VideoSpider
from classcard_dataclient.models.video import Video


class VideoSync(BaseSync):
    def __init__(self):
        super(VideoSync, self).__init__()
        self.page_list = [("http://www.qlshx.sdnu.edu.cn/", "gyss.htm")]
        self.video = []

    def crawl(self):
        for page in self.page_list:
            print(">>> start crawl {}".format(page))
            vs = VideoSpider(page[0], page[1])
            vs.start()
            for target in vs.targets.values():
                if isinstance(target["content"], str):
                    video = Video(name=target["topic"], path=target["content"])
                else:
                    video = Video(name=target["topic"], path=target["content"][0])
                self.video.append(video)

    def sync(self):
        self.crawl()
        for video in self.video:
            self.client.create_video(self.school_id, video)
