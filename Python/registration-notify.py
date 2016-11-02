import urllib
import smtplib
from email.mime.text import MIMEText
import time

def seats(crn):
	gatech = urllib.urlopen("https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_detail_sched?term_in=201702&crn_in="+str(crn))
	test = gatech.read()
	test = test.split('\n')

	done = False; lineNum = 0; name = ''
	for i in range(len(test)):
		line = test[i]
		if line.find('<th CLASS="ddlabel" scope="row" >')!=-1 and name=='':
			name = line[line.find('-'):line.find('<br')]
			name = name[10:]
		if line.find('>Seats<')!=-1:
			done = True;lineNum=i; break

	if done==True:
		total = test[lineNum+1][22:test[lineNum+1][1:].find('<')+1]
		taken = test[lineNum+2][22:test[lineNum+2][1:].find('<')+1]
		remain = test[lineNum+3][22:test[lineNum+3][1:].find('<')+1]
		waitlist = test[lineNum+8][22:test[lineNum+8][1:].find('<')+1]

		if waitlist == '0': waitlist = ''

		isopen = ''
		if remain!='0' and waitlist =='': isopen = 'Open'

		# print 'Total\tTaken\tRemain\n%s\t\t%s\t\t%s'%(total,taken,remain)
		return [name,str(crn),total,taken,remain,waitlist,isopen]
	gatech.close()

def textAlert(subject,contents):
    me = '77evan@gmail.com'
    you = '4074054234@mms.att.net'

    s = smtplib.SMTP('localhost')


#	msg = MIMEText(contents)
#	msg['Subject'] = subject
#	msg['From'] = me
#	msg['To'] = you
#
#	# Send the message via our own SMTP server, but don't include the
#	# envelope header.
#	s = smtplib.SMTP('smtp.gmail.com',587)
#	s.starttls();
#	s.login(me,'password')
#
#	s.sendmail(me, you, msg.as_string())
#	s.quit()


#classes = [27499,24357,20482,22696,30200,24413]
#backup = [20476,20479,22717,22713,22715,20929]
#backup2 = [22720,21071,21068]

#total = [classes,backup,backup2]
total = [[26619, 29149]]
# total = [[22696,30200,22717,22713,22715],[27139,27129],[22720,21071]]

out = 'Class\t\t\t\tCRN\t\t\tTotal\tTaken\tRemain\tWait\tOpen'
tableOld = []

try:
    for i in total:
        out+='\n'
        for j in i:
            classs = seats(j)
            tableOld.append(classs)
            out+='\n' + '\t\t'.join(classs)
    print out
except:
    print 'No connection'

textAlert("test1", "test2")

# print '\nChanges:\n'

# tableOld[0][4] = '23'

# while True:
# 	time.sleep(30)
# 	tableNew = []
# 	try:
# 		for i in total:
# 			out+='\n'
# 			for j in i:
# 				classs = seats(j)
# 				tableNew.append(classs)
# 		if len(tableNew)!=len(tableOld):
# 			print 'Error'
# 		else:
# 			change = False
# 			for i in range(len(tableNew)):
# 				if tableOld[i][4]!=tableNew[i][4]:
# 					print '\n' + '\t\t'.join(tableNew[i]) + '\t\tFrom: ' + tableOld[i][4]
# 					change = True
# 					textout = tableNew[i][0]+' from ' + tableOld[i][4] + ' to ' + tableNew[i][4]
# 					textAlert('There has been a change',textout)
# 			if not change:
# 				print 'Same'
# 			else:
# 				print
# 			tableOld = tableNew

# 	except:
# 		print 'No connection'

