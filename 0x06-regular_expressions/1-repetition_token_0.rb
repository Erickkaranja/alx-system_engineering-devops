#!/usr/bin/env ruby
# matches above tokens.

puts ARGV[0].scan(/so{2,5}l/).join
