require "erb"

html = %{<!DOCTYPE html>
<html lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
        <title>mock exam</title>
        <script src="../assets/quizdown/quizdown.js"></script>
        <script>quizdown.init();</script>
    </head>
    <body>
        <div class="quizdown">
            ---
            primaryColor: "#181d37"
            shuffleQuestions: true
            shuffleAnswers: true
            nQuestions: 50
            ---
            <%- File.readlines('quiz/questions.md').each do |line| -%>
            <%= line %>
            <%- end -%>
        </div>
    </body>
</html>}

File.open("mock_exam.html", "w") do |file|
    file.write(ERB.new(html, trim_mode: "-").result(binding))
end
