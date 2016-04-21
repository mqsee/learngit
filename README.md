## 实习入门任务
### 代码包
#### old_version中存放的是
leetcode文件夹中：leetcode上面基础的几道题目的源码
tf-idf_static:使用lib库和正则表达式爬取十篇新闻并计算TF-IDF的代码。
(编写时间:4.7-4.12)

#### new_version中是更新以后的代码。
leetcode已更新
1.使用了enumerate
2.使用python内部自带字符串翻转函数s[::-1]
3.使用了list的reverse，append，sum，sorted等函数
tf-idf_static:使用HTTP request请求，BeautifulSoup提取新闻标题和内容
统计TF-IDF选取每篇新闻的top10保存到json文件中

### 功能详解
#### leetcode文件夹中内容
1.字符串操作
https://leetcode.com/problems/reverse-words-in-a-string/
对应reverse.py 实现字符串的翻转
https://leetcode.com/problems/valid-palindrome/
对应palindrome.py 判断一个字符串是否是回文串

2.Hash操作
https://leetcode.com/problems/two-sum/
对应two-sum.py 寻找两个数之和等于target

3.List操作
https://leetcode.com/problems/pascals-triangle/
对应triangle1.py 输出图形
https://leetcode.com/problems/pascals-triangle-ii/
对应triangle2.py 输出图形

4.递归
https://leetcode.com/problems/majority-element/
对应majority-element.py 寻找数组中众数
https://leetcode.com/problems/maximum-subarray/
对应maxSubArray.py 输出最大连续子串和