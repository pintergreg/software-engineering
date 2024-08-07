chapters = []
File.readlines('lectures/SUMMARY.md').each do |line|
    next unless m = line.strip.match(/\[.*\]\((lectures\/.+\.md)\)/)
    chapters.push m.captures[0]
end
