inputs = Dir.glob('*.html').filter{|x| x =~ /^[0-9]{2}_.+\.html/}

inputs.each do |x|
    # puts "#{x} #{x.gsub(".html", ".pdf")}"
    `npx decktape reveal --headless new --chrome-path /bin/chromium #{x} #{x.gsub(".html", ".pdf")}`
end
