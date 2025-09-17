Dir.glob('*.md').filter{|x| x =~ /^[0-9]{2}_.+\.md$/}.each do |x|
    `ruby build.rb -m #{x}`
end
