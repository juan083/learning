#!/usr/bin/python3
# -*- coding:UTF-8 -*-

'''
对两个英文文档进行统计，使用了多少单词，每个单词的使用频率；
对两个英文文档进行比较，返回有差异的行和内容
'''

class docHelper(object):

    lineA = []

    wordsA = []

    lineB = []

    wordsB = []

    # 读取文件内容
    def readDoc(self):
        fileA = open('./a.txt', 'r')
        txtA = fileA.read()
        self.lineA = txtA.splitlines()
        for txt in self.lineA:
            self.wordsA.extend([v.strip() for v in txt.split(' ')])

        fileB = open('./b.txt', 'r')
        txtB = fileB.read()
        self.lineB = txtB.splitlines()
        for txt in self.lineB:
            self.wordsB.extend([v.strip() for v in txt.split(' ')])

        return

    # 统计单词
    def getWordCount(self):
        dicA = {}
        for v in self.wordsA:
            if v in dicA:
                dicA[v] += 1
            else:
                dicA[v] = 1
        dicB = {}
        for v in self.wordsB:
            if v in dicB:
                dicB[v] += 1
            else:
                dicB[v] = 1
        return dicA, len(list(dicA.keys())), dicB, len(list(dicB.keys()))

    def docDiff(self):
        ret = []
        lineCountA = len(self.lineA)
        lineCountB = len(self.lineB)
        lineCount = max(lineCountA, lineCountB)
        for line in range(0, lineCount):
            txtA = self.lineA[line] if lineCountA >= line + 1 else ""
            txtB = self.lineB[line] if lineCountB >= line + 1 else ""
            if txtA != txtB:
                ret.append([line, txtA, txtB])
        return ret

helper = docHelper()
helper.readDoc()
dicA, countA, dicB, countB = helper.getWordCount()
print('文档A，单词频率', dicA)
print('文档B，单词频率', dicB)

print('文档A，单词总数（不同）', countA)
print('文档B，单词总数（不同）', countB)

docDiff = helper.docDiff()
print('不同的行', len(docDiff))
for l in docDiff:
    print('第%d行，a内容:%s，b内容:%s' % (l[0], l[1], l[2]))
