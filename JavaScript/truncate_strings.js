// Challenge:
// Create a function that takes three arguments (txt, txt_length, txt_suffix) and returns a truncated string.

// txt: Original string.
// txt_length: Truncated length limit.
// txt_suffix: Optional suffix string parameter.
// Truncated returned string length should adjust to passed length in parameters regardless of length of the suffix.

function truncate(txt, txt_length, txt_suffix = null){
	if (txt_suffix == null){
		return txt.substring(0,txt_length);
	}
	return txt.substring(0,txt_length-txt_suffix.length).concat(txt_suffix);
}