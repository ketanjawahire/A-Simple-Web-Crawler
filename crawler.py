#!/usr/bin/python

import httplib
import sys
import re
from HTMLParser import HTMLParser


class miniHTMLParser( HTMLParser ):
  viewedQueue = []
  instQueue = []
  
  def get_next_link( self ):
    if self.instQueue == []:
      return ''
    else:
      return self.instQueue.pop(0)

  def gethtmlfile( self, site, page ):
    try:
      httpconn = httplib.HTTPConnection(site)
      httpconn.request("GET", page)
      resp = httpconn.getresponse()
      resppage = resp.read()
    except:
      resppage = ""
    return resppage

  def handle_starttag( self, tag, attrs ):
    if tag == 'a':
      newstr = str(attrs[0][1])
      if re.search('http', newstr) == None :
        if re.search('mailto', newstr) == None:
          if (  re.search('ap',newstr)!=None or re.search('aro',newstr)!=None or re.search('asax',newstr)!=None or re.search('ascx',newstr)!=None or re.search('ashx',newstr)!=None or re.search('asmx',newstr)!=None or re.search('asp',newstr)!=None or re.search('aspx',newstr)!=None or re.search('asr',newstr)!=None or re.search('att',newstr)!=None or re.search('awm',newstr)!=None or re.search('axd',newstr)!=None or re.search('bml',newstr)!=None or re.search('bok',newstr)!=None or re.search('browser',newstr)!=None or re.search('bwp',newstr)!=None or re.search('cdf',newstr)!=None or re.search('cfm',newstr)!=None or re.search('cfml',newstr)!=None or re.search('cha',newstr)!=None or re.search('chat',newstr)!=None or re.search('chm',newstr)!=None or re.search('cms',newstr)!=None or re.search('con',newstr)!=None or re.search('cshtml',newstr)!=None or re.search('csp',newstr)!=None or re.search('dbm',newstr)!=None or re.search('dhtml',newstr)!=None or re.search('dml',newstr)!=None or re.search('do',newstr)!=None or re.search('dochtml',newstr)!=None or re.search('docmhtml',newstr)!=None or re.search('ece',newstr)!=None or re.search('fcgi',newstr)!=None or re.search('hdm',newstr)!=None or re.search('hdml',newstr)!=None or re.search('htc',newstr)!=None or re.search('htm',newstr)!=None or re.search('html',newstr)!=None or re.search('hype',newstr)!=None or re.search('jhtml',newstr)!=None or re.search('jsp',newstr)!=None or re.search('jspx',newstr)!=None or re.search('mht',newstr)!=None or re.search('mhtml',newstr)!=None or re.search('mspx',newstr)!=None or re.search('ognc',newstr)!=None or re.search('php',newstr)!=None or re.search('php3',newstr)!=None or re.search('php4',newstr)!=None or re.search('php5',newstr)!=None or re.search('phtm',newstr)!=None or re.search('phtml',newstr)!=None or re.search('rhtml',newstr)!=None or re.search('sht',newstr)!=None or re.search('shtm',newstr)!=None or re.search('shtml',newstr)!=None or re.search('vbd',newstr)!=None or re.search('vbhtml',newstr)!=None or re.search('wml',newstr)!=None or re.search('xht',newstr)!=None or re.search('xhtm',newstr)!=None or re.search('xhtml',newstr)!=None or re.search('',newstr)!=None ):
            if (newstr in self.viewedQueue) == False:
              print "  adding", newstr
              self.instQueue.append(newstr)
              self.viewedQueue.append( newstr )
          else:
            print "  ignoring", newstr
        else:
          print "  ignoring", newstr
      else:
        print "  ignoring", newstr

def main():
  linkqueue=[]
  if sys.argv[1] == '':
    print "usage is ./minispider.py site link"
    sys.exit(2)
  mySpider = miniHTMLParser()
  link = sys.argv[2]
  while link != '':
    print "\nChecking link ", link
    # Get the file from the site and link
    retfile = mySpider.gethtmlfile( sys.argv[1], link )
    # Feed the file into the HTML parser
    mySpider.feed(retfile)
    # Search the retfile here
    # Get the next link in level traversal order
    link = mySpider.get_next_link()
    linkqueue.append(link)
  mySpider.close()
  print "\ndone\n"
  for member in linkqueue:
    print member+'\n'
if __name__ == "__main__":
  main()

