"""
\A 字符串左边界, 左边不可有字符
\Z 字符串右边界, 右边不可有字符
^  与\A一致, 多行匹配下可表示一行文字的左边界
$  与\Z一致, 多行匹配下可表示一行文字的右边界
边界符号不与任何字符匹配
"""
# \\b 单词的左右边界
# \B 此处不可是单词边界
import 正则表达式函数 as F
c = (r'search\b')
F.search(c,'searcha')
F.search(c,'search aaa')
