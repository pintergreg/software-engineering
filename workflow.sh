# compile presentaion
cd lectures
ruby build_slides.rb
cd ..
cd practicals
ruby build_slides.rb
cd ..

# compile handout
ruby build.rb
mdbook build

# compile mindmap
npx markmap-cli -o lectures/mindmap.html --offline --no-open lectures/mindmap.md

# build mock exam
cd lectures
ruby build_mock_exam.rb
cd ..

# copy slides
mkdir -p book/slides/figures
mkdir -p book/slides/assets
cp -r lectures/figures/* book/slides/figures/
cp -r lectures/*.html book/slides/
cp -r practicals/*.html book/slides/
cp -r assets/* book/assets/
