#targetengine "session"try{    var docs_key = app.activeDocument.fullName    var hub = app.docs[docs_key].hub    }catch(e){    app.debug('\t' + e.report().split('\n').join('\n\t'));    var hub = app.hub;    }if(hub.show() === 0){    hub.execute()    }