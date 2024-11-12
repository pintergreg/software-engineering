require "fileutils"

def collect_summaries()
    result = []
    Dir.glob('./summary_week*.md') do |x|
        result.push x
    end
    return result.sort
end

def write_header()
    File.open("summary_full.md", "a") do |fp|
        File.readlines("summary_header.md").each do |line|
            fp.write line
        end
    end
end

def write_content()
    summaries = collect_summaries
    summaries.each do |summary|
        preamble = false
        refs = false
        File.readlines(summary).each_with_index do |line, i|
            refs = true if line.start_with? "# references"
            
            File.open("summary_full.md", "a") do |fp|
                if not preamble and i > 0 and not refs
                    fp.write line
                end
            end
            
            preamble = !preamble if line.strip == "---"
        end
    end
end

def write_references()
    File.open("summary_full.md", "a") do |fp|
        fp.write "# references\n\n"
        fp.write "::: {#refs .text-smaller}\n"
        fp.write ":::\n"
    end
end

def generate_full_summary()
    FileUtils.remove_file "summary_full.md", force=true
    write_header
    write_content
    write_references
end

if $PROGRAM_NAME == __FILE__
    generate_full_summary
end
