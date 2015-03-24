#mongosion

===========================================


####[https://github.com/grasses/mongosion](https://github.com/grasses/mongosion)


#####An easy session module, writed by python base on pymongo using for tornado.py or web.py!

##### See introduction here [http://homeway.me/2014/08/28/mongosion/](http://homeway.me/2014/08/28/mongosion/)

#Installation

===========================================

###use pip
 
	pip install mongosion
	
###or source

	wget https://pypi.python.org/packages/source/m/mongosion/mongosion-0.1.3.tar.gz

	tar -zxvf mongosion-0.1.3.tar.gz
	
	cd mongosion-0.10/
	
	sudo python setup.py install
	
#mongosion


=========================================

####mongosion give you 5 function: 
	
`get( session_id )`  => get session

`delete( session_id )`  => remove session
	
`save( session_id, {})` => save sesssion
	
`exist( session_id )` => check session is existion

`expired()` => delete expired sessions


####data type 

	{'_id':'', 'time':'', 'session': {'uid':'', 'status':'', ......} } 

#####setting
	setting = {
    	# mongodb setting
    	'host':'localhost',
    	'port': 27017,
    	'databse':'mongosion',
    	
    	#session setting
    	'session_id': '',
    	'sessionExpires': 24*60*60,
    	'autoDeleteExpired': True, # clean expired sessions at every get 
    	'secretKey':base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
    	'session' : { 'uid':'520', 'status':'useing', 'isLogin':False } # default type of data
	}

### how to work

![process](http://xiaocao.u.qiniudn.com/image/mongsosionProcessSession.png)

### mongosion.get(session_id)

![process](http://xiaocao.u.qiniudn.com/image/mongsosionGetSession.png)

### mongosion.save(session_id, {'uid':'', 'isLogin': True})

![process](http://xiaocao.u.qiniudn.com/image/mongsosionSaveSession.png)

#Warning

=========================================

####remember install pymongo && run mongodb

<br>

#License
 

=========================================
 
 
####GPL
 
 
 
