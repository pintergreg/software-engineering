require "fileutils"

inputs = []
Dir.glob('./summary_week*.md') do |x|
    inputs.push x
end
inputs.sort!

FileUtils.remove_file "summary_full.md", force=true
preamble = false
File.readlines('summary_week01.md').each_with_index do |line, i|
    File.open("summary_full.md", "a") do |fp|
        if not preamble and i > 0
            fp.write line
        end
    end
    if line.strip == "---"
        preamble = !preamble
        # p line, i, preamble
    end
 
end
