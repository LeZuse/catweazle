#include "string_sprintf.jsx"

String.prototype.toTitleCase = function(){
	return this.split(' ').map(function(word){
		word = word.toLowerCase();
		word = word.split('');
		if(word.length > 0){
			word[0] = word[0].toUpperCase();
			}
		
		word = word.join('');	
		return word
		}).join(' ')
	}	

app.addons.push('String.prototype.toTitleCase');
// -------------------------------------------------------------------------- //


String.prototype.multiReplace = function (flags,  hash) {
	var str = this;
	for (key in hash) {
		str = str.replace( new RegExp(key, flags), hash[key] );
	}
	return str;
};

app.addons.push('String.prototype.multiReplace');
