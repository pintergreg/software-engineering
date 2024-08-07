# frozen_string_literal: true

require 'fileutils'

@target = 'src'

chapters = []
File.readlines('lectures/SUMMARY.md').each do |line|
  next unless m = line.strip.match(%r{\[.*\]\((lectures/.+\.md)\)})

  chapters.push m.captures[0]
end

FileUtils.rm_r @target if Dir.exist?(@target)
FileUtils.mkdir_p "#{@target}/lectures"


FileUtils.cp('lectures/SUMMARY.md', "#{@target}/")
chapters.each do |x|
  `pandoc #{x} -f markdown -t commonmark -o #{@target}/#{x} -L assets/exclude_elements.lua`
end
