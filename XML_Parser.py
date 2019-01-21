#!/usr/bin/env python
# encoding: utf-8
import os
from lxml import etree, objectify
class xmlParser(object):
    def __init__(self, path, *args, **kwargs):
        self.path = path
        self.protocolFilenameList    = []
        self.systemRequirementList   = []
        self.srsRequirementList      = []
        self.textStringList          = []
        self.protocolList            = {}
        self.protocolDict            = {}
        self.systemRequirementDict   = {}
        self.srsRequirementDict      = {}
        self.textStringDict          = {}
        self.protocolHeaderStyle     = '<w:pPr><w:pStyle w:val="Heading3"/>'
        self.systemRequirementStyle  = '<w:pPr><w:pStyle w:val="Rqmt-0-Name-Trace"/>'
        self.srsRequirementStyle     = '<w:pPr><w:pStyle w:val="Rqmt-0-Name"/>'
        self.textStringStyle         = '<w:pPr><w:pStyle w:val="Rqmt-0-Name-String"/>'
        #self.systemRequirementStyle  = "Rqmt-0-Name-Trace"
        #self.srsRequirementStyle     = "Rqmt-0-Name"
        #self.textStringStyle         = "Rqmt-0-Name-String"
        self.getProtocolFilenameList()
        self.sortProtocolList()
        self.addRequirementListToProtocolDictionary()
        self.sortSystemRequirementList()
        self.createSystemRequirementTable()
        self.sortSrsRequirementList()
        self.createSrsRequirementTable()
        self.sortTextStringList()
        self.createTextStringTable()
        return super(xmlParser, self).__init__(*args, **kwargs)
 
    def getProtocolFilenameList(self): 
        self.protocolFilenameList = [fileName for fileName in os.listdir(self.path)]

    ## Read the protocol names from each file: 
    def getProtocolList(self, path):
        protocolHeader = ''
        lines = []
        try:
            f = open(path, 'r')
            lines = f.readlines()
            f.close()
        except IOError:
            return
        char = ''
        for line in lines:
            if self.protocolHeaderStyle in line:
                protocolHeader = ''
                line = line[line.find(self.protocolHeaderStyle)+ len(self.protocolHeaderStyle):]
                content = line[:line.find('</w:p>')]
                line = line[line.find('</w:p>'):]
                if content.find('</w:pPrChange>') == -1:
                    while 1:
                        if content.find('<w:t>')>0:
                            content = content[content.find('<w:t>')+ len('<w:t>'):]
                            protocolHeader += content[:content.find('</w:t>')].strip()
                            content = content.lstrip(protocolHeader)
                        elif content.find('<w:t xml:space="preserve">')>0:
                            content = content[content.find('<w:t xml:space="preserve">')+ len('<w:t xml:space="preserve">'):]
                            protocolHeader += content[:content.find('</w:t>')].strip()
                            content = content.lstrip(protocolHeader)
                        else:
                            break
                return protocolHeader
            
    ## Read the system reqirements from the single protocol file 
    #def getRequirementList(self, path, requirementType):
    #    lst = []
    #    lstsring = []
    #    tree = etree.parse(path)
    #    root = tree.getroot()
    #    body = root.find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}body')
    #    for element in body.iter(tag=etree.Element):
    #        if element.attrib:
    #            for key in element.attrib:
    #                if element.attrib[key] == requirementType:
    #                    lst.append(element.getparent().getparent())
    #    for item in lst:
    #        tempstring = ''
    #        for elmt in item.itertext():
    #            tempstring += elmt
    #        if tempstring:
    #            lstsring.append(tempstring)
    #    return sorted(set(lstsring))    
    
    def getRequirementList(self, path, requirementType):
        lst = []
        lines = []
        try:
            f = open(path, 'r')
            lines = f.readlines()
            f.close()
        except IOError:
            return
        for line in lines:
            while line.find(requirementType) > 0:
                tempstring = ''
                line = line[line.find(requirementType)+ len(requirementType):]
                content = line[:line.find('</w:p>')]
                line = line[line.find('</w:p>'):]
                if content.find('</w:pPrChange>') == -1:
                    while 1:
                        if content.find('<w:t>')>0:
                            content = content[content.find('<w:t>')+ len('<w:t>'):]
                            tempstring += content[:content.find('</w:t>')].strip()
                            content = content.lstrip(tempstring)
                        elif content.find('<w:t xml:space="preserve">')>0:
                            content = content[content.find('<w:t xml:space="preserve">')+ len('<w:t xml:space="preserve">'):]
                            tempstring += content[:content.find('</w:t>')].strip()
                            content = content.lstrip(tempstring)
                        else:
                            break
                if tempstring and tempstring != 'na':
                    lst.append(tempstring)
        return sorted(set(lst))

    ## Sorted the protocol names from all protocols
    def sortProtocolList(self):
        for protocol in self.protocolFilenameList:
            self.protocolList.update({protocol : self.getProtocolList(os.path.join(self.path, protocol))})

    ## Sorted the system requirements from all protocols
    def sortSystemRequirementList(self):
        for key in self.protocolDict:
            for value in self.protocolDict[key][0]:
                if value not in self.systemRequirementList:
                    self.systemRequirementList.append(value)
        return self.systemRequirementList.sort()

    ## Sorted the SRS requirements from all protocols
    def sortSrsRequirementList(self):
        for key in self.protocolDict:
            for value in self.protocolDict[key][1]:
                if value not in self.srsRequirementList:
                    self.srsRequirementList.append(value)
        return self.srsRequirementList.sort()

    ## Sorted the Text String from all protocols
    def sortTextStringList(self):
        for key in self.protocolDict:
            for value in self.protocolDict[key][2]:
                if value.upper() not in self.textStringList:
                    self.textStringList.append(value.upper())
        return self.textStringList.sort()

    ## Create a protocol dictinoary with system requirements
    def addRequirementListToProtocolDictionary(self):
        for protocol in self.protocolFilenameList:
            sysrqmt = self.getRequirementList(os.path.join(self.path, protocol), self.systemRequirementStyle)
            srsrqmt = self.getRequirementList(os.path.join(self.path, protocol), self.srsRequirementStyle)
            textString = self.getRequirementList(os.path.join(self.path, protocol), self.textStringStyle)
            self.protocolDict.update({self.protocolList[protocol] : [sysrqmt, srsrqmt, textString]})

    ## Create a systme requirement dictionary with protocols
    def addProtocolListToRequirementDictionary(self, rqmtDict, rqmt, lst):
        rqmtDict.update({rqmt : lst})

    ## Create the System Requirement Table
    def createSystemRequirementTable(self):
        for rqmt in self.systemRequirementList:
            lst = []
            for key in self.protocolDict:
                for value in self.protocolDict[key][0]:
                    if value == rqmt:
                        lst.append(key)
            self.addProtocolListToRequirementDictionary(self.systemRequirementDict, rqmt, lst)

    ## Create the SRS Requirement Table
    def createSrsRequirementTable(self):      
        for rqmt in self.srsRequirementList:
            lst = [] 
            for key in self.protocolDict:
                for value in self.protocolDict[key][1]:
                    if value == rqmt:
                        lst.append(key)
            self.addProtocolListToRequirementDictionary(self.srsRequirementDict, rqmt, lst)

    ## Create the Text String Table
    def createTextStringTable(self):      
        for rqmt in self.textStringList:
            lst = [] 
            for key in self.protocolDict:
                for value in self.protocolDict[key][2]:
                    if value.upper() == rqmt:
                        lst.append(key)
            self.addProtocolListToRequirementDictionary(self.textStringDict, rqmt, lst)

    ## Print out the table 
    def printList(self, table):
        for key in sorted(table):
            print key,'\n' , table[key],'\n'
    
    def getTable(self, dictionary):
        table = []
        for key in sorted(dictionary, key=str.lower):
            table.append([key, dictionary[key]])
        return table
    
#path = r'C:\Users\bing.ma\Desktop\INOmax\Plan A\_3-1-5-formal\Phase_1'


#srs_d = {}
#sy_d = {}
#ts_d = {}
#srs = ['boot-up-screen-ikaria', 'customer-alarm-high-priority', 
#       'customer-alarm-low-priority', 'customer-alarm-speaker',
#       'diagnostic-service-log', 'fault-alarm-system-shutdown', 
#       'startup-sw-version', 'upgrade-browser-firmware']
#sy = ['SY-connect-service', 'SY-fail-resolve-condition', 
#      'SY-identify-software', 'SY-STD-60601-1-8-iec']

#ts = []
#for key in xml.srsRequirementDict:
#    for i in srs:
#        if i == key:
#            xml.srsRequirementDict[key].sort()
#            srs_d.update({key: xml.srsRequirementDict[key]})

#for key in xml.systemRequirementDict:
#    for i in sy:
#        if i == key:
#            xml.systemRequirementDict[key].sort()
#            sy_d.update({key: xml.systemRequirementDict[key]})

#for key in xml.textStringDict:
#    for i in ts:
#        if i == key:
#            xml.textStringDict[key].sort()
#            ts_d.update({key: xml.textStringDict[key]})

#f = open('srs addition.txt', 'w')
#for key in sorted(srs_d):
#    f.write(key + '\n')
#    for i in srs_d[key]:
#        f.write('--------' + i + '\n')
#    f.write('\n')
#f.close()


#f = open('SY rqmt list jp.txt', 'w')
#for key in sorted(sy_d):
#    f.write(key + '\n')
#    for i in sy_d[key]:
#        f.write('--------' + i + '\n')
#    f.write('\n')

#f.close()

#f = open('text string rqmt list jp.txt', 'w')
#for key in sorted(ts_d):
#    f.write(key + '\n')
#    for i in ts_d[key]:
#        f.write('--------' + i + '\n')
#    f.write('\n')

#f.close()