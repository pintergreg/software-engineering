inputs = [
    "00_intro.md",
    "01_sdlc.md",
    "02_scrum.md",
    "03_kanban.md",
    "04_requirement_analysis.md",
    "05_user_story_mapping.md",
    "06_uml.md",
    "07_c4.md",
    "08_patterns.md",
    "09_interfaces.md",
    "10_planning.md",
    "11_wireframing.md",
    "12_clean_code.md",
    "project.md",
]
Dir.glob('./summary_week*.md') do |x|
    inputs.push x
end
inputs.each do |x|
    `ruby build.rb -m #{x}`
end
