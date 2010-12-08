String.prototype.multiReplace = function (flags,  hash) {
	var str = this;
	for (key in hash) {
		str = str.replace( new RegExp(key, flags), hash[key] );
	}
	return str;
};

app.addons.push('String.prototype.multiReplace');
