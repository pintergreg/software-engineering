require 'optparse'
require 'yaml'

options = YAML.load_file('build_config.yaml')
puts options

#options[:reveal_url] = "http://127.0.0.1/reveal.js-5.1.0/"
# options[:self_contained] = true

OptionParser.new do |parser|
  parser.banner = 'Usage: build.rb [options]'

  parser.on('-m', '--markdown INPUT', 'Provide MARKDOWN filename') do |i|
    options[:markdown] = i
    if i.end_with? '.md'
      options[:markdown] = i[..-4]
    end
  end
  parser.on('--bibliography BIBLIOGRAPHY', 'Provide BIBLIOGRAPHY file') do |bibliography|
    options[:bibliography] = bibliography
  end
  parser.on('--csl CSL', 'Provide CSL file') do |csl|
    options[:csl] = csl
  end
  parser.on('-s', '--self-contained', 'Pass self-contained argument to pandoc') do |_s|
    options[:self_contained] = true
  end
  parser.on('--reveal-url REVEALURL', 'RevealJS URL') do |url|
    options[:reveal_url] = "-V revealjs-url:\"#{url}\""
  end
end.parse!

p options
if options[:markdown] == "README"
  exit(0)
end

if options[:self_contained]
  `pandoc -f markdown+tex_math_double_backslash -t revealjs #{options[:markdown]}.md --standalone --slide-level 2 --css #{options[:assets]}/custom.css -o #{options[:markdown]}_embedded.html --citeproc --csl #{options[:cls]} --bibliography #{options[:bibliography]} --bibliography wikipedia.bib --mathml --embed-resources #{options[:reveal_url]}`
else
  `pandoc -f markdown+tex_math_double_backslash -t revealjs #{options[:markdown]}.md --standalone --slide-level 2 --css #{options[:assets]}/custom.css -o #{options[:markdown]}.html --citeproc --csl #{options["csl"]} --bibliography #{options["bibliography"]} --bibliography wikipedia.bib --mathml #{options[:reveal_url]} -H #{options["assets"]}/custom_header.html -A #{options["assets"]}/custom_after_body.html `#-L #{options[:assets]}/highlight_code.lua`
  # `pandoc -f markdown+tex_math_double_backslash -t revealjs #{options[:markdown]}.md --standalone --slide-level 2 --css #{options[:assets]}/custom.css -o #{options[:markdown]}_print.html --citeproc --csl #{options[:cls]} --bibliography #{options[:bibliography]} --bibliography wikipedia.bib --bibliography wikipedia.bib --mathml #{options[:reveal_url]}`
end
 # -L ../assets/revealjs-codeblock.lua
