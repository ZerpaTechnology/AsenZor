# -*- coding: utf-8 -*-
try:
 from ztec.zdb import DB
except:
 from zdb import DB
db=DB()
db.load=True
db('users').campo('username',db.str,True,True,False,False,0,-1,None,None)
db('users').campo('email',db.email,False,True,False,False,0,-1,None,None)
db('users').campo('password',db.password,False,True,False,False,0,-1,None,None)
db('users').campo('token',db.str,True,True,False,False,0,-1,None,None)
db('users').campo('expediente',db.int,True,True,False,False,0,-1,None,None)
db('users').campo('ip´s',db.list,False,True,False,False,0,-1,None,None)
db('users').campo('login',db.bool,False,True,False,False,0,-1,None,None)
db('noticias').campo('autor',db.str,False,True,False,False,0,-1,None,None)
db('noticias').campo('titulo',db.str,False,True,False,False,0,-1,None,None)
db('noticias').campo('img',db.file,False,True,False,False,0,-1,None,None)
db('noticias').campo('noticia',db.doc,False,True,False,False,0,-1,None,None)
db('noticias').campo('fecha',db.datetime,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M')
db('noticias').campo('fechaModificación',db.datetime,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M')
db('tokens').campo('user',db.str,False,True,False,False,0,-1,None,None)
db('tokens').campo('value',db.str,False,True,False,False,0,-1,None,None)
db('tokens').campo('nace',db.datetime,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M')
db('tokens').campo('muere',db.datetime,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M')
db('tokens').insertar('jesus', 'zWm-Q(G<', 'datetime:22/1/2017 15:15', 'datetime:22/1/2017 19:15')
db('users').insertar('jesus', 'mailto:jesus26abraham1996@gmail.com', 'password:123', 'zWm-Q(G<', 2015147042, ['127.0.0.1'], False)
db('users').relacionar(0,'token',campo= 'value',id= 0,tabla= 'tokens',)
db('users').relacionar(0,'username',tabla= 'tokens',id= 0,campo= 'user',)
db.load=False
