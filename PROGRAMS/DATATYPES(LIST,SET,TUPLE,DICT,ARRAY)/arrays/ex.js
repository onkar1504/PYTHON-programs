function MostFreeTime(str) {
	var dates = [];
	str.split(",").forEach(d => {
		dt = d.substring(1, d.length - 1).split("-");

		s = dt[0];
		dt[0] = s.substr(s.length - 2, 2) == "AM" ? s.substr(0, 5) :
			(Number.parseInt(s.substr(0, 2)) < 12 ? Number.parseInt(s.substr(0, 2)) + 12 + ":" + s.substr(3, 2) : s.substr(0, 5));

		s = dt[1];
		dt[1] = s.substr(s.length - 2, 2) == "AM" ? s.substr(0, 5) :
			(Number.parseInt(s.substr(0, 2)) < 12 ? Number.parseInt(s.substr(0, 2)) + 12 + ":" + s.substr(3, 2) : s.substr(0, 5));

		dates.push({
			from: Date.parse("2018-01-01T" + dt[0] + ":00.000Z"),
			to: Date.parse("2018-01-01T" + dt[1] + ":00.000Z")
		})
	});

	dates.sort(function (dt1, dt2) {
		return dt2.from < dt1.from
	})

	max = Number.MIN_VALUE;
	for (var i = dates.length - 1; i > 0; i--) {
		diff = dates[i].from - dates[i - 1].to;
		if (diff > max) max = diff;
	}

	d = new Date(max);
	return d.toISOString().substr(11, 5);
}