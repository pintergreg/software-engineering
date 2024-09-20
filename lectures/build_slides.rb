inputs = [
    "00_intro.md",
    "01_sdlc.md",
    "02_scrum.md",
    "03_kanban.md",
    "04_requirement_analysis.md"
]
Dir.glob('./summary_week*.md') do |x|
    inputs.push x
end
inputs.each do |x|
    `ruby build.rb -m #{x}`
end
