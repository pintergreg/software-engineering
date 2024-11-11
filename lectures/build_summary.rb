require "fileutils"

def collect_summaries()
    result = []
    Dir.glob('./summary_week*.md') do |x|
        result.push x
    end
    return result.sort
end


FileUtils.remove_file "summary_full.md", force=true
preamble = false
refs = false
File.readlines('summary_week01.md').each_with_index do |line, i|
    if line.start_with? "# references" then
        refs = true
    end
    File.open("summary_full.md", "a") do |fp|
        if not preamble and i > 0 and not refs
            fp.write line
        end
    end
    if line.strip == "---"
        preamble = !preamble
        # p line, i, preamble
    end
 
end
