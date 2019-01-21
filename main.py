#!/usr/bin/env python
# encoding: utf-8

import os
from XML_Parser import xmlParser
from DOCX_Parser import docxParser
from DOCX_Creator import DocxWrite, Document

class vcri(object):
    def __init__(self, srsPath, protocolPath, *args, **kwargs):
        self.srsFile = docxParser(srsPath)
        self.protocolFile = xmlParser(protocolPath)
        self.srsFileTextStrings = self.getList(self.srsFile.textStringList)
        self.protocolFileTextStrings = self.getList(self.protocolFile.textStringList)
        self.srsFileSrsRequirements = self.getList(self.srsFile.srsRequirementList)
        self.protocolFileSrsRequirements = self.getList(self.protocolFile.srsRequirementList)
        self.srsFileSystemRequirements = self.getList(self.srsFile.systemRequirementList)
        self.protocolFileSystemRequirements = self.getList(self.protocolFile.systemRequirementList)
        self.listFilter(self.srsFileTextStrings)
        self.listFilter(self.srsFileSrsRequirements)
        self.listFilter(self.srsFileSystemRequirements)
        self.unusedTextStrings = self.getUsedList(self.srsFileTextStrings, self.protocolFileTextStrings)
        self.unusedSrsRequirements = self.getUsedList(self.srsFileSrsRequirements, self.protocolFileSrsRequirements)
        self.unusedSystemRequirements = self.getUsedList(self.srsFileSystemRequirements, self.protocolFileSystemRequirements)
        self.undesignatedTextStrings = self.getUndesignatedList(self.srsFileTextStrings, self.protocolFileTextStrings)
        self.undesignatedSrsRequirements = self.getUndesignatedList(self.srsFileSrsRequirements, self.protocolFileSrsRequirements)
        self.undesignatedSystemRequirements = self.getUndesignatedList(self.srsFileSystemRequirements, self.protocolFileSystemRequirements)
        self.writeFile()
        return super(vcri, self).__init__(*args, **kwargs)
    
    def getUsedList(self, srslist, protocollist):
        unusedlist = []
        for item in srslist:
            if item not in protocollist:
                unusedlist.append(item)
        return unusedlist
    
    def getUndesignatedList(self, srslist, protocollist):
        undesignatedList = []
        for item in protocollist:
            if item not in srslist:
                undesignatedList.append(item)
        return undesignatedList

    def getList(self, lst):
        templst = []
        for item in lst:
            templst.append(item)
        return templst

    def printList(self, list):
        for i in list:
            print i

    def listFilter(self, lst):
        filterItems = [' {BL}', ' {MR}', ' (H)', ' {3.1.5 and later}', ' {prior to 3.1.5}']
        for i in range(len(lst)):
            for j in range(len(filterItems)):
                if filterItems[j] in lst[i]:
                    imp = lst[i].replace(filterItems[j], '')
                    lst[i] = imp.strip()
                    break
                
    def traceProtocols(self, undesignatedrqmt, dic):
        lst = []
        for key in dic:
            if key == undesignatedrqmt:
                lst.append(dic[key])
        return lst
    
    def writeFile(self):
        f = open('vcri.txt', 'w')
        f.write('                  VCRI REPORT\r\n')
        f.write('                ---------------\r\n\r\n\r\n\r\n')

        f.write('List of Text Strings from protocols\r\n')
        f.write('====================================== \r\n')
        for line in self.protocolFileTextStrings:
            f.write(line + '\r\n')
        f.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\r\n\r\n')

        f.write('List of unused Text Strings\r\n')
        f.write('====================================== \r\n')
        for line in self.unusedTextStrings:
            f.write(line + '\r\n')
        f.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\r\n\r\n')

        f.write('List of SRS Requirements from protocols\r\n')
        f.write('====================================== \r\n')
        for line in self.protocolFileSrsRequirements:
            f.write(line + '\r\n')
        f.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\r\n\r\n')

        f.write('List of unused SRS Requirements\r\n')
        f.write('====================================== \r\n')
        for line in self.unusedSrsRequirements:
            f.write(line + '\r\n')
        f.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\r\n\r\n')

        f.write('List of System Requirements from protocols\r\n')
        f.write('====================================== \r\n')
        for line in self.protocolFileSystemRequirements:
            f.write(line + '\r\n')
        f.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\r\n\r\n')

        f.write('List of unused System Requirements\r\n')
        f.write('====================================== \r\n')
        for line in self.unusedSystemRequirements:
            f.write(line + '\r\n')
        
        f.close()

    def writeSrsRequirementFlie(self):
        DocxWrite('VCRI SRS Requirements', self.protocolFile.srsRequirementDict)

    def writeSystemRequirementFlie(self):
        DocxWrite('VCRI System Requirements', self.protocolFile.systemRequirementDict)

    def writeTextStringFlie(self):
        DocxWrite('VCRI Text String', self.protocolFile.textStringDict)

def searchSRSfile(path):
    if path:
        for fileName in os.listdir(path):
            if 'SRS' in fileName:
                return fileName


def checkPath(mesg):
    while 1:
        path = os.path.join(raw_input(mesg))
        if os.path.exists(path):
            if 'SRS' in mesg:
                tmp = searchSRSfile(path)
                if tmp:
                    return os.path.join(path, tmp)
                else:
                    print 'Invalid path'
            else:
                return path
        else:
            print 'Invalid path'
            
def main():
    
    protocolPath = checkPath("Type or copy/paste the protocols folder path.\r\n")
    srsPath = checkPath("Type or copy/paste the SRS folder path.\r\n")

    doc = vcri(srsPath, protocolPath)
    doc.writeFile()
    print "File created in the current folder as vcri.txt"
    raw_input("Press any key to continue.....")

    

if __name__ == "__main__":
    
    main()
