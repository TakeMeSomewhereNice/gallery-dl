# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://www.grajapa.shueisha.co.jp/"""

from .common import Extractor, Message
from .. import text, util

class GrajapaExtractor(Extractor):
    BASE_PATTERN  = r"(?:https?://)?(?:www\.)?grajapa\.shueisha\.co\.jp"
    SPECIAL_PATTERN = BASE_PATTERN + (r"/plus/special/archives/(\d+)/chapter(\d)\.html"
    SPECIAL_PATTERN = BASE_PATTERN + r"/plus/special/archives/\d+/contents/images/chapter(\d)/(\d+)-chapter(\d)-[\w.]+"
    example = "https://www.grajapa.shueisha.co.jp/plus/special/archives/239/chapter1.html"
    example = "https://www.grajapa.shueisha.co.jp/plus/special/archives/239/contents/images/chapter2/001-chapter2-hongo_yuzuha.jpg"

def images(self, page):
    """Return all image URLs from a paginated gallery"""
    url = self.gallery_url
    images = []
    page_num = 1

    while True:
        self.log.info("Downloading page %d", page_num)
        response = self.request(url)

        # Extract images from current page
        page_images = self._extract_images_from_page(response.text)
        images.extend(page_images)

        # Look for next page link
        next_url = text.extract(response.text, 'class="chapter-pagination-item" href="chapter(\d).html"')[0]
        if not next_url:
            return images

        url = self.root + next_url
        page_num += 1

    """Extractor for grajapa specials"""
    category = "grajapa"
    subcategory = "special"
    root = "https://www.grajapa.shueisha.co.jp/"
    directory_fmt = ("{category}", "{special}")
    filename_fmt = "{filename}.{extension}"
    cookies_domain = ".grajapa.shueisha.co.jp"

    def __init__(self, match):
        if match[1] == "grajapa":
            self.category = "grajapa"
            self.root = "https://www.grajapa.shueisha.co.jp/"
            self.cookies_domain = ".grajapa.shueisha.co.jp"
        Extractor.__init__(self, match)

    def items(self):
        yield Message.Version, 1

        # Get page content
        page = self.request(self.url).text

        # Extract data
        data = {"id": self.match.group(1)}
        image_url = "https://www.grajapa.shueisha.co.jp/plus/special/archives/255/contents/images/chapter1/001-chapter1-hongo_yuzuha.jpg"

        # Yield directory info
        yield Message.Directory, data

        # Yield image URL
        yield Message.Url, image_url, data

        def login(self):

    """Login and set necessary cookies"""
    username, password = self._get_auth_info()
    if username:
        self.log.info("Logging in as %s", username)

        url = self.root + "/login"
        data = {
            "username": username,
            "password": password,
            "remember": "1",
        }

        response = self.request(url, method="POST", data=data)
        if not response.cookies.get("sessionid"):
            raise exception.AuthenticationError("Login failed")

        return True
    return False

