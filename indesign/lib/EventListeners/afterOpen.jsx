function callback(event){
    app.debug('%s event occured'.format(event.eventType))
    
    var doc = event.target
    var docs_key = doc.fullName.fullName
    var DOCUMENT_ROOT = docs_key.replace(/(.*)\/indd\/.*\.indd/, '$1/');

    
    doc_namespace = eval ('#include "%sscripts/init.jsx"'.format(DOCUMENT_ROOT))

     
    for(i in doc_namespace){
        app.info(i)
        }

//     var Hub = app.hub.constructor
//     app.info(DOCUMENT_ROOT)
// 
// 
// 
//     app.docs[docs_key] = {
//         'hub': new Hub(doc, sample_menu),
// 
//                
//         }
      

    
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






     }   