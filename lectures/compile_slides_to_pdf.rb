require 'optparse'

options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: example.rb [options]"

  opts.on("-s", "--selected PATH", "Select slides to compile") do |x|
    options[:selected] = x
  end
end.parse!

if options.include? :selected
    `npx decktape reveal --headless new --chrome-path /bin/chromium #{options[:selected]} #{options[:selected].gsub(".html", ".pdf")}`
else
    inputs = Dir.glob('*.html').filter{|x| x =~ /^[0-9]{2}_.+\.html/}

    inputs.each do |x|
        # puts "#{x} #{x.gsub(".html", ".pdf")}"
        `npx decktape reveal --headless new --chrome-path /bin/chromium #{x} #{x.gsub(".html", ".pdf")}`
    end
end
