from gmail import GMail, Message

mail = GMail('tranduccuong.c4e21','Cuong26990')
body = '''
<p>Em đi xa qu&aacute;, <strong>em đi xa anh qu&aacute;.</strong></p>
<p>&nbsp;</p>
<p><em><strong>Em đi xa anh qu&aacute;</strong></em></p>
'''


msg = Message('Don xin nghi',to='tranduccuong90@gmail.com', text=body)
mail.send(msg)