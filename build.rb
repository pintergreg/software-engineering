# frozen_string_literal: true

require 'fileutils'

@target = 'src'

chapters = []
File.readlines('lectures/SUMMARY.md').each do |line|
  next unless m = line.strip.match(%r{\[.*\]\((lectures/.+\.md)\)})

  chapters.push m.captures[0]
end

FileUtils.rm_r @target if Dir.exist?(@target)
FileUtils.mkdir_p @target
