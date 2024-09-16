inputs = [
    "00_intro.md",
    "01_sdlc.md",
    "02_previously.md",
    "02_scrum.md",
    "03_kanban.md"
]
inputs.each do |x|
    `ruby build.rb -m #{x}`
end
