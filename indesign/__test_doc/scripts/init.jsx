(function(){

var document_settings = {
    LOGGING: true,
    LOGGING_INFO: true,
    LOGGING_DEBUG: true,
    LOGGING_WARNING: true,
    LOGGING_ERROR: true,
    LOGGING_CRITICAL: true,



//     observer: function(item){
//         app.info(item.eventCode);
//         try{
//             var callback = app.docs[docs_key][item.eventSource.label].apid[item.eventCode]  // access to docs_key
//              }
//         catch(e){
//             app.info('No callback for APID %s'.format(item.eventCode))
//             }
//         if(callback){
//             callback(item.eventSource);
//             }
//         },

    apid: {
        'twin': {
            subjectModified: function(item){ 
                var objects =  item.labeledPageItems('twin');
                var angle = item.eventSource.rotationAngle;
                
                
                
                objects.each(function(obj){ 
                    app.info(obj.constructor.name);
                    obj.rotationAngle = angle; 
                    });
                }
            },
            
        'test': {
            'subjectCreated': app.info,
            'subjectDelete': app.info,
            'subjectDeselected': app.info,
            'subjectSelected': function(){ app.info('hugli') },
            'subjectFileChanged': app.info,
            'subjectLoadContextMenu': app.info,
            'subjectModified': alert,
            'subjectModified-text': app.info,
            'subjectModified-recomposed-overset': app.info,
            'subjectModified-recomposed-nooverset': app.info,
            'subjectScriptTagChanged': app.info,
            'subjectModified-usertyping': app.info
            },
        '': {
            'docSelected': app.info,
            'docDeselected': app.info,
            'docLoaded': app.info
            }
        },


    menu: {    "q": {name: 'Document menu',
            'c': ['check for updates', function(){ app.info('checking for updates ...') }], 
            'u': ['update database', 'update_database']}}
    }            
    return document_settings
    }());