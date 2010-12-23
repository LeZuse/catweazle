function callback(event){
   
    var doc = event.target
    
    if (doc.constructor.name === 'Document'){
        var docs_key = doc.fullName.fullName    
        var DOCUMENT_ROOT = docs_key.replace(/(.*)\/indd\/.*\.indd/, '$1/');
        
        try{
            var doc_namespace = eval ('#include "%sscripts/init.jsx"'.format(DOCUMENT_ROOT))
            }
        catch(e){ app.error(e) }
    
        var Hub = app.hub.constructor
    
    
        app.docs[docs_key] = {
            'hub': new Hub(doc, doc_namespace.menu),            
        observer: function(item){
            app.info(item.eventCode);
            try{
                var callback = app.docs[docs_key].apid[item.eventSource.label][item.eventCode]  // access to docs_key
                 }
            catch(e){
                app.info('No callback for APID %s on %s\n%s'.format(item.eventCode, item.eventSource.label, e))
                }
            if(callback){
                callback(item);
                }
            },
            
            'apid': doc_namespace.apid
            }
        }
    }
   
   
   
   
   
   
   
   
   
   
    
// 	var doc = app.documents[app.documents.length - 1]; // Last opened document
// 	var docPath = String(doc.fullName).split('/');
// 	var initDocPath = '/Volumes/' + docPath.cut('1:-2').join('/') + '/scripts/initDoc.jsx';
// 	
// 	try{ app.doScript(File(initDocPath),ScriptLanguage.JAVASCRIPT, [doc]); }
// 	
// 	catch(e){		
// 		var msg = [
// 			'Could not execute initDoc',
// 			(e.line || '???'),
// 			e.name,
// 			e.message
// 			];
// 		app.growl(msg.join('\n'), true);		
// 		
// 		}    
