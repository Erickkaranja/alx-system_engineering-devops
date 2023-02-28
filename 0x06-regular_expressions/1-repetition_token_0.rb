#!/usr/bin/env ruby
# matches above tokens.
puts ARGV[0].scan(/hbtt{1,4}n/).join
