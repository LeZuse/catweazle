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
    //function callback(event){
    eval('#include "../lib/EventListeners/%s.jsx"'.format(event_name));
        //}
    app.addEventListener(event_name, callback, false) ;
    });

app.info('All event listeners are set up');