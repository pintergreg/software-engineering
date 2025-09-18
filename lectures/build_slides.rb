load "build_summary.rb"

inputs = Dir.glob('*.md').filter{|x| x =~ /^[0-9]{2}_.+\.md$/}

Dir.glob('./summary_week*.md') do |x|
    inputs.push x
end
generate_full_summary
inputs.push "summary_full.md"
inputs.each do |x|
    `ruby build.rb -m #{x}`
end
