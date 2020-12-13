import re
import xml.etree.ElementTree as etree

from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension

HTML = """
<div class="video-container drop-shadow">
  <div class="video-dialog" data-source="{video_id}">
    <div>
      <p>
        Watching embedded videos will transfer data to YouTube. To protect your privacy, you need to accept <a href="https://policies.google.com/privacy" target="_blank">YouTubes privacy statement and terms of use</a> first by clicking the button below.
      </p>
      <input type="button" class="button button-primary video-button" value="Accept &amp; Play" />
      <a href="{video_url}" class="button button-secondary">Direct Link</a>
    </div>
  </div>
</div>
"""

RE_YOUTUBE = re.compile(r"^https?://www\.youtube\.com/watch\?v=(\w+)")

class VideoInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        video_url = m.group("url")
        match = RE_YOUTUBE.match(video_url)
        if not match:
            raise ValueError("Found non-youtube URL '{}' in video tag".format(video_url))
        el = etree.fromstring(HTML.format(
            video_url=video_url,
            video_id=match.group(1),
        ))
        return el, m.start(0), m.end(0)


class VideoExtension(Extension):
    def extendMarkdown(self, md):
        VIDEO_PATTERN = r"@Video\((?P<url>[^)]*)\)"
        processor = VideoInlineProcessor(VIDEO_PATTERN, md)
        md.inlinePatterns.register(processor, "video", 175)


def makeExtension(**kwargs):
    return VideoExtension(**kwargs)
