# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, print_function, unicode_literals
from corpuscrawler.util import crawl_korero_html, crawl_udhr


def crawl(crawler):
    out = crawler.get_output(language='ccp')
    crawl_udhr(crawler, out, filename='udhr_ccp.txt')
    for book in ('fulbareng', 'pacchan', 'shikya_pudhi', 'tui_ebe_vili'):
        crawl_korero_html(crawler, out, project='corpora-ccp',
                          genre='Literature',
                          filepath='ccp_%s.html' % book)