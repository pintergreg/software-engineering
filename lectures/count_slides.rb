require 'pdf-reader'

inputs = Dir.glob('*.pdf').filter{|x| x =~ /^[0-9]{2}_.+\.pdf/}

puts "pdf,page_count"
inputs.each do |x|
  reader = PDF::Reader.new(x)

  puts "#{x},#{reader.page_count}"
end
