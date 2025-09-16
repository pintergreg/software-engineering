inputs = [
    "02_user_story.md",
]
inputs.each do |x|
    `ruby build.rb -m #{x}`
end
