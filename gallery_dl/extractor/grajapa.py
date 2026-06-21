# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://www.grajapa.shueisha.co.jp/"""

from .common import Extractor, Message
from .. import text

class GrajapaExtractor(Extractor):
    """Extractor for grajapa specials"""
    category = "grajapa"
    subcategory = "special"
    directory_fmt = ("{category}", "{special}")
    filename_fmt = "{tim} {filename}.{extension}"

    pattern = (BASE_PATTERN +
               r"(plus/special/archives/\d+/contents/images/chapter(\d)/(\d+)-chapter(\d)-[\w.]+)")
    example = "https://www.grajapa.shueisha.co.jp/plus/special/archives/239/contents/images/chapter2/001-chapter2-hongo_yuzuha.jpg"

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

