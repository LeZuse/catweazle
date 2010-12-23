function callback(event){
    app.debug('%s event occured'.format(event.eventType))
   
    var doc = event.target
    
    if (doc.constructor.name === 'Document'){       
        var docs_key = event.target.fullName
        delete app.docs[docs_key]
        }
    }