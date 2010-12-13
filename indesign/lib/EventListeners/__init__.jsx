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
    import_command = '#include "%slib/EventListeners/%s.jsx"'.format(app.ROOT_DIRECTORY, event_name)
    



    try{
        //function callback(event){
        eval(import_command)
        //}
        
        var guarded_callback = function(event){
            try{
                callback(event);
                }
            catch(e){
                app.error('error, when executing %s callback'.format(event.eventType))
                app.debug('\t' + e.report().split('\n').join('\n\t'))
                app.debug('STACK\n\t' + $.stack.split('\n').join('\n\t'))
                }
            }
        
        app.addEventListener(event_name, guarded_callback, false) ;
        }
        
    catch(e){ 
        app.error('%s event listener was not set up!'.format(event_name))
        app.debug('\t' + e.report().split('\n').join('\n\t'))
        app.debug('STACK\n\t' + $.stack.split('\n').join('\n\t'))
        }
        
    });

app.info('Finished event listeners set-up');