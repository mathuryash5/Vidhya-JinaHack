__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

from typing import Dict, List

from jina.executors.crafters import BaseCrafter, BaseSegmenter
from numpy import character



class Splitter(BaseCrafter):

    def craft(self, text: str, *args, **kwargs) -> Dict:
        cord_uid, title = text.split('#')
        # text = title + ". " + abstract
        return dict(weight=1.0, text=title, meta_info=cord_uid.encode('utf8'))