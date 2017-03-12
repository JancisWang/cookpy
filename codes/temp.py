#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Life's pathetic, let's happy coding everyday ♡~ Nasy.

@author: Nasy
@date: Mar 11, 2017
@email: sy_n@me.com
@file: temp.py
@license: MIT

Copyright © 2017 by Nasy. All Rights Reserved.
"""
from typing import Tuple, Dict, Any
import pprint

DATA_TUPLE: Tuple[Tuple[str, Any], ...] = (
    ("type", "text"),
    ("collection", "group message"),
    ("time", "1488844812123"),
    ("title", "An Emoji"),
    ("from", (("name", "Nasy"), ("id", "nasy"))),
    ("to", (("name", "可愛いです"), ("id", "g_07"))),
    (
        "mentioned", [(("name", "C.C."), ("id", "cc")), (("name", "benny"),
                                                         ("id", "bey"))]),
    # 注意这里的 "\u2005" 不是一个空格
    # 这是微信@人之后的那个空出来的东西，真实的哟
    ("data", "@C.C.\u2005@benny\u2005ヽ(。_°)ノ"))


def parser() -> Dict[str, Any]:
    """Parsing the raw data."""
    return {
        i[0]: {j[0]: j[1]
               for j in i[1]}
        if type(i[1]) is tuple else ([{k: l
                                       for k, l in j} for j in i[1]]
                                     if type(i[1]) is list else i[1])
        for i in DATA_TUPLE
    }


def main() -> None:
    """Main function."""
    data = parser()
    pprint.pprint(data)
    print()
    for i in data.items():
        print(*i, sep=': ')


if __name__ == "__main__":
    main()
