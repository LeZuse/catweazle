app.menus[0].submenus.item('Cat&weazle').remove();app.scriptMenuActions.everyItem().remove();var menuRoot = app.menus[0].submenus.add('Cat&weazle');var reloadStandardLibrary = app.scriptMenuActions.add("reinit");reloadStandardLibrary.eventListeners.add("onInvoke", function(){ app.doScript(File(app.ROOT_DIRECTORY + '/init_application.jsx'), ScriptLanguage.JAVASCRIPT) }, false);menuRoot.menuItems.add(reloadStandardLibrary);	app.info('All Menu entries are set up')// 	var reloadInitDoc = app.scriptMenuActions.add("Reload initDoc");// 	reloadInitDoc.eventListeners.add("onInvoke", fReloadInitDoc, false);// 	menuRoot.menuItems.add(reloadInitDoc);    	// 	function fReloadInitDoc(){// 		var doc  = app.activeDocument;// 		var docPath = String(doc.fullName).split('/');// 		var initDocPath = '/Volumes/' + docPath.cut('1:-2').join('/') + '/scripts/initDoc.jsx';		// 		// 		try{ // 			app.doScript(File(initDocPath), ScriptLanguage.JAVASCRIPT, [doc]); // 			app.growl('initDoc reloaded for %s'.sprintf(doc.fullName))// 			}// 		catch(e) {app.growl(e.report())}// 		}	