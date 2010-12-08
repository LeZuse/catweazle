app.eventListeners.everyItem().remove();

var event_names = [
    "afterClose", "beforeClose",
    "afterExport", "beforeExport",
    "afterImport", "beforeImport",
    "afterNew", "beforeNew",
    "afterOpen", "beforeOpen",
    "afterPrint", "beforePrint",
    "afterRevert", "beforeRevert",
    "afterSave", "beforeSave",
    "afterSaveACopy", "beforeSaveACopy",
    "afterSaveAs", "beforeSaveAs"
    ];

/* CS5 only
* "beforeQuit"
* "afterQuit"
*/


event_names.each(function(event_name){    
    try{
        //function callback(event){
        eval('#include "./lib/EventListeners/%s.jsx"'.format(event_name));
            //}
        app.addEventListener(event_name, callback, false) ;
        }
        
    catch(e){ 
        app.error('%s event listener was not set up!'.format(event_name))
        app.debug('\t' + e.report().split('\n').join('\n\t'))
        app.debug('STACK\n\t' + $.stack.split('\n').join('\n\t'))
        }
        
    });

app.info('Finished event listeners set-up');