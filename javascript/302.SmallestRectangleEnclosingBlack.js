/**
 * @param {character[][]} image
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var minArea = function(image, x, y) {
	top    = first(0, x,               (x) => image[x].includes('1'));
	bottom = first(x, image.length,    (x) => !image[x].includes('1'));
	left   = first(0, y,               (y) => image.some((row) => row[y] === '1'));
	right  = first(y, image[0].length, (y) => image.every((row) => row[y] !== '1'));
	return (bottom - top) * (right - left);
};
var first = function(lo, hi, check) {
	while (lo < hi) {
		let mid = Math.floor((lo + hi) / 2);
		if (check(mid)) hi = mid;
		else lo = mid + 1;
	}
	return lo;
};