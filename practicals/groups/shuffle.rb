students = File.readlines('students.txt', chomp: true)

rng = Random.new(42)
shuffled = students.shuffle(random: rng).each_slice(5).to_a

teams = ["viewport", "sculpting", "animation", "projection/trajectory", "operation"]

teams.zip(shuffled).each do |team, student_group|
    puts team
    puts student_group
end
