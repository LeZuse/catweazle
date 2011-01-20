#targetengine 'session'


CW = {};




(function(){
	var documentRoot = $.fileName.split('/').cut(':-2').join('/')
	
	CW['prefs'] = function(){
	var output = [];
	
	
	
	return output
	}();
	
	
	// Environment
	var subFolders = ['lib', 'act', 'ui'];
	loadModules(subFolders);
	//------------------------------------------------


	//Set-up InDesign Document eventListeners
	var documentEventListeners = {
		'beforeSave': CW.sync_commit_changes,
		};
	setUpEventListeners(doc, documentEventListeners);	
	//------------------------------------------------
	
	//Set-up APID event callbacks
	var APIDcallbacks = {
		Pricebox: {		
			'subjectCreated': undefined,
			'subjectDelete': undefined,
			'subjectDeselected': undefined,
			'subectFileChanged': undefined,
			'subjectLoadContextMenu': undefined,
			'subjectModified': undefined,
			'subjectModified-text': undefined,
			'subjectModified-recomposed-overset': CW.sync_write_changes,
			'subjectModified-recomposed-nooverset': CW.sync_write_changes,
			'subjectScriptTagChanged': undefined,
			'subjectModified-usertyping': CW.sync_write_changes
			},
		TextFrame: {
			'subjectCreated': undefined,
			'subjectDelete': undefined,
			'subjectDeselected': undefined,
			'subectFileChanged': undefined,
			'subjectLoadContextMenu': undefined,
			'subjectModified': undefined,
			'subjectModified-text': undefined,
			'subjectModified-recomposed-overset': undefined,
			'subjectModified-recomposed-nooverset': undefined,
			'subjectScriptTagChanged': undefined,
			'subjectModified-usertyping': undefined
			},
		box: {
			'subjectCreated': undefined,
			'subjectDelete': undefined,
			'subjectDeselected': undefined,
			'subectFileChanged': undefined,
			'subjectLoadContextMenu': undefined,
			'subjectModified': undefined,
			'subjectModified-text': undefined,
			'subjectModified-recomposed-overset': undefined,
			'subjectModified-recomposed-nooverset': undefined,
			'subjectScriptTagChanged': undefined,
			'subjectModified-usertyping': undefined			
			},
		document: {
			'docSelected': undefined,
			'docDeselected': undefined,
			'docLoaded': CW.sync_read_updates
			}
		};		
		setUpApidCallbacks();
		//------------------------------------------------
		




// Functions --------------------------------------------------------------------------//	
	
	function loadModules(subFolders){
		try{
			var scriptsFolder = documentRoot + '/scripts/';
			subFolders.each(function(subFolder){
				var plugsPath = scriptsFolder + subFolder + '/';
				var plugins = Folder(plugsPath).getFiles('*.jsx');
				
				
				plugins.each(function(plugin){
					try{
						eval('#include "' + plugin + '"');
						}
					catch(e){
						app.growl(e.report('Failed Plugin Import ' + plugin), true);
						}
					});
				
				
				});
			}
			
		catch(e){
			app.growl(e.report('Failed setting-up environment'), true);	
			}				
		}
		
	//------------------------------------------------
	
	
	function setUpEventListeners(doc, documentEventListeners){	
		doc.eventListeners.everyItem().remove();
		
		for(var documentEvent in documentEventListeners){
			doc.addEventListener(documentEvent, documentEventListeners[documentEvent],false);
			}
		}
		
	//------------------------------------------------
	
	
	function setUpApidCallbacks(){	
		CW.observer = function(item){
			var log = File(documentRoot + '/logs/APIDevents.log');
			log.open('e');
			log.seek(0, 2);
			log.write(item.eventSource.label + ': ' +  item.eventCode + '\r');
			log.close();
			try{
				var callback = APIDcallbacks[item.eventSource.label][item.eventCode];
				}
			catch(e){
				try{
					var callback = APIDcallbacks['document'][item.eventCode];
					}
				catch(e){
					app.growl(e.report('????'), true);
					}
				}
			if(callback){
				callback(item.eventSource);
				}
			}
		}
		
	//------------------------------------------------		
	})();





		




