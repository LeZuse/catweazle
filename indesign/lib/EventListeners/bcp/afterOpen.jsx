function callback(event){
    app.debug('%s event occured: (%s)'.format(event.eventType, event.eventPhase))
    
//     var doc = event.target
//     var docs_key = doc.fullName.fullName    
//     var DOCUMENT_ROOT = docs_key.replace(/(.*)\/indd\/.*\.indd/, '$1/');
//  
//     var doc_namespace = eval ('#include "%sscripts/init.jsx"'.format(DOCUMENT_ROOT))
// 
//     var Hub = app.hub.constructor
// 
// 
//     app.docs[docs_key] = {
//         'hub': new Hub(doc, doc_namespace['menu'])               
//         }
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
