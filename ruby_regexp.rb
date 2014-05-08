re = /(\d+):(\d+)/     # match a time hh:mm
md = re.match("Time: 12:34am")
md.type	»	MatchData
md[0]         # == $&	»	"12:34"
md[1]         # == $1	»	"12"
md[2]         # == $2	»	"34"
md.pre_match  # == $`	»	"Time: "
md.post_match # == $'	»	"am"


re = /(\d+):(\d+)/     # match a time hh:mm
md1 = re.match("Time: 12:34am")
md2 = re.match("Time: 10:30pm")
md1[1, 2]	»	["12", "34"]
md2[1, 2]	»	["10", "30"]